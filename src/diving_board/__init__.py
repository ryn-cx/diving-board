import logging
import re
from pathlib import Path
from typing import Any, override

import requests
from gapi import AbstractGapiClient

from diving_board.adjacent_series import AdjecentSeariessMixin
from diving_board.constants import DIVING_BOARD_PATH
from diving_board.exceptions import HTTPError
from diving_board.schedule import ScheduleMixin
from diving_board.season import SeasonMixin
from diving_board.vod import VodMixin

default_logger = logging.getLogger(__name__)

TIMEOUT = 30


class DivingBoard(
    AbstractGapiClient,
    SeasonMixin,
    AdjecentSeariessMixin,
    ScheduleMixin,
    VodMixin,
):
    @override
    def client_path(self) -> Path:
        return DIVING_BOARD_PATH

    def __init__(
        self,
        timezone: str = "America/Los_Angeles",
        logger: logging.Logger = default_logger,
    ) -> None:
        self.timezone = timezone
        self.logger = logger

        self.cached_api_key = ""
        self.public_token = ""
        self.access_token = ""
        self.cached_authorization_token = ""
        self.cached_realm = ""

        # TODO: Implement actually using refresh_token.
        self.refresh_token = ""

        self.api_domain = "https://dce-frontoffice.imggaming.com"
        self.domain = "https://www.hidive.com"
        super().__init__()

    def _get_api_key(self) -> str:
        url = f"{self.domain}/code/js/app.8decd4739abfe3a59a45.js"
        self.logger.info("Downloading api key: %s", url)
        headers = {"Origin": self.domain, "Referer": self.domain}
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        response_text = response.text

        if not (match := re.search(r'API_KEY:"([0-9a-f-]+)"', response_text)):
            msg = "Failed to extract token from bundle.js"
            raise ValueError(msg)

        self.cached_api_key = match.group(1)
        return self.cached_api_key

    def _api_key(self) -> str:
        if not self.cached_api_key:
            self._get_api_key()

        return self.cached_api_key

    def _get_authorization(self) -> None:
        """Get various authorization tokens from the second layer of authentication."""
        url = (
            f"{self.api_domain}/api/v1/init/"
            "?lk=language"
            "&pk=subTitleLanguage"
            "&pk=audioLanguage"
            "&pk=autoAdvance"
            "&pk=pluginAccessTokens"
            "&pk=videoBackgroundAutoPlay"
            "&readLicences=true"
            "&countEvents=LIVE"
            "&menuTargetPlatform=WEB"
            "&readIconStore=ENABLED"
        )
        self.logger.info("Downloading second auth layer: %s", url)
        headers = {
            "Origin": self.domain,
            "Referer": self.domain,
            "x-api-key": self._api_key(),
        }
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        json_response = response.json()
        self.cached_realm = json_response["settings"]["realm"]
        authentication = json_response["authentication"]
        self.cached_authorization_token = authentication["authorisationToken"]
        self.refresh_token = authentication["refreshToken"]

    def _authorization_token(self) -> str:
        if not self.cached_authorization_token:
            self._get_authorization()

        return self.cached_authorization_token

    def _realm(self) -> str:
        if not self.cached_realm:
            self._get_authorization()

        return self.cached_realm

    def _download_api_request(
        self,
        endpoint: str,
        params: dict[str, Any],
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        if headers is None:
            headers = {}
        headers["authorization"] = f"Bearer {self._authorization_token()}"
        headers["x-api-key"] = self._api_key()
        headers["Origin"] = self.domain
        headers["Referer"] = self.domain
        headers["Realm"] = self._realm()

        url = f"{self.api_domain}/{endpoint}"

        request = requests.Request("GET", url, params=params)
        prepared = request.prepare()
        self.logger.info("Downloading API data: %s", prepared.url)
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=TIMEOUT,
        )

        if response.status_code != 200:  # noqa: PLR2004
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        return response.json()
