import json
import logging
import re
import uuid
from pathlib import Path
from typing import Any

import requests
from gapi import (
    AbstractGapiClient,
    GapiCustomizations,
    apply_customizations,
    update_json_schema_and_pydantic_model,
)

from diving_board.constants import DIVING_BOARD_PATH, FILES_PATH
from diving_board.exceptions import HTTPError
from diving_board.other_seasons import OtherSeasonsMixin
from diving_board.other_seasons.models import OtherSeasons
from diving_board.season import SeasonMixin
from diving_board.season.models import Season

RESPONSE_MODELS = OtherSeasons | Season

default_logger = logging.getLogger(__name__)


class DivingBoard(AbstractGapiClient, SeasonMixin, OtherSeasonsMixin):
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

    def save_file(self, name: str, data: dict[str, Any]) -> None:
        """Add a new test file for a given endpoint."""
        input_folder = FILES_PATH / name
        new_json_path = input_folder / f"{uuid.uuid4()}.json"
        new_json_path.parent.mkdir(parents=True, exist_ok=True)
        new_json_path.write_text(json.dumps(data, indent=2))

    def update_model(
        self,
        name: str,
        customizations: GapiCustomizations | None = None,
    ) -> None:
        """Update a specific response model based on input data."""
        schema_path = DIVING_BOARD_PATH / f"{name}/schema.json"
        model_path = DIVING_BOARD_PATH / f"{name}/models.py"
        files_path = FILES_PATH / name
        update_json_schema_and_pydantic_model(files_path, schema_path, model_path, name)
        apply_customizations(model_path, customizations)

    def files_path(self) -> Path:
        """Get the path to the files directory."""
        return FILES_PATH
