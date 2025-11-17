import json
import logging
import re
from typing import Any

import requests
from gapi import GapiCustomizations
from pydantic import ValidationError

from diving_board.constants import FILES_PATH
from diving_board.exceptions import HTTPError
from diving_board.other_seasons import OtherSeasonsMixin
from diving_board.other_seasons.models import OtherSeasons
from diving_board.season import SeasonMixin
from diving_board.season.models import Season
from diving_board.update_files import save_file, update_model

RESPONSE_MODELS = OtherSeasons | Season

default_logger = logging.getLogger(__name__)


class DivingBoard(SeasonMixin, OtherSeasonsMixin):
    def __init__(self, logger: logging.Logger = default_logger) -> None:
        self.logger = logger
        self.api_key = ""
        self.public_token = ""
        self.access_token = ""
        self.refresh_token = ""
        self.authorization_token = ""
        self.realm = ""
        self.api_domain = "https://dce-frontoffice.imggaming.com"
        self.domain = "https://www.hidive.com"

    def _get_api_key(self) -> str:
        if self.api_key:
            return self.api_key

        url = f"{self.domain}/code/js/app.8decd4739abfe3a59a45.js"
        self.logger.info("Downloading api key: %s", url)
        response = requests.get(
            url,
            headers={
                "Origin": self.domain,
                "Referer": self.domain,
            },
            timeout=30,
        )
        response_text = response.text

        if not (match := re.search(r'API_KEY:"([0-9a-f-]+)"', response_text)):
            msg = "Failed to extract token from bundle.js"
            raise ValueError(msg)

        self.api_key = match.group(1)
        return self.api_key

    def _get_second_layer_authorization(self) -> str:
        """Get various authorization tokens from the second layer of authentication."""
        url = (
            f"{self.api_domain}/api/v1/init/?lk=language&pk=subTitleLanguage"
            "&pk=audioLanguage&pk=autoAdvance&pk=pluginAccessTokens&pk=videoBackgroundAutoPlay"
            "&readLicences=true&countEvents=LIVE&menuTargetPlatform=WEB&readIconStore=ENABLED"
        )
        self.logger.info("Downloading second auth layer: %s", url)
        response = requests.get(
            url,
            headers={
                "Origin": self.domain,
                "Referer": self.domain,
                "x-api-key": self._get_api_key(),
            },
            timeout=30,
        )
        json_response = response.json()
        self.authorization_token = json_response["authentication"]["authorisationToken"]
        self.refresh_token = json_response["authentication"]["refreshToken"]
        self.realm = json_response["settings"]["realm"]
        return self.authorization_token

    def _get_authorization_bearer(self) -> str:
        if not self.authorization_token:
            self._get_second_layer_authorization()

        return self.authorization_token

    def _get_realm(self) -> str:
        if not self.realm:
            self._get_second_layer_authorization()

        return self.realm

    def _get_api_request(
        self,
        endpoint: str,
        params: dict[str, Any],
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        if headers is None:
            headers = {}
        headers["authorization"] = f"Bearer {self._get_authorization_bearer()}"
        headers["x-api-key"] = self._get_api_key()
        headers["Origin"] = self.domain
        headers["Referer"] = self.domain
        headers["Realm"] = self._get_realm()

        url = f"{self.api_domain}/{endpoint}"
        self.logger.info("Downloading API data: %s", url)
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=30,
        )

        if response.status_code != 200:  # noqa: PLR2004
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        return response.json()

    def _parse_response[T: RESPONSE_MODELS](
        self,
        response_model: type[T],
        data: dict[str, Any],
        name: str,
        customizations: GapiCustomizations | None = None,
    ) -> T:
        try:
            parsed = response_model.model_validate(data)
        except ValidationError as e:
            save_file(name, data)
            update_model(name, customizations)
            msg = "Parsing error, model updated, try again."
            raise ValueError(msg) from e

        if self.dump_response(parsed) != data:
            save_file(name, data)
            temp_path = FILES_PATH / "_temp"
            named_temp_path = temp_path / name
            named_temp_path.mkdir(parents=True, exist_ok=True)
            original_path = named_temp_path / "original.json"
            parsed_path = named_temp_path / "parsed.json"
            original_path.write_text(json.dumps(data, indent=2))
            parsed_path.write_text(json.dumps(self.dump_response(parsed), indent=2))
            msg = "Parsed response does not match original response."
            raise ValueError(msg)

        return parsed

    def dump_response(self, data: RESPONSE_MODELS) -> dict[str, Any]:
        """Dump an API response to a JSON serializable object."""
        return data.model_dump(mode="json", by_alias=True, exclude_unset=True)
