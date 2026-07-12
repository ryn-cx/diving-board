"""Contains the DivingBoard class."""

import time
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from diving_board.adjacent_series import SeriesAdjacentTo
from diving_board.constants import BASE_API_URL
from diving_board.exceptions import HTTPError
from diving_board.schedule import Schedule
from diving_board.schedule import ScheduleGroupList as ScheduleGroupList
from diving_board.search import Search
from diving_board.season import Season
from diving_board.series import Series
from diving_board.vod import Vod

logger = getLogger(__name__)
logger.addHandler(NullHandler())

USER_AGENT = (
    "Mozilla/5.0 (Linux; Android 10; K) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/134.0.0.0 Mobile Safari/537.3"
)


class DivingBoard:
    """HiDive API wrapper."""

    MAIN_DOMAIN = "hidive.com"
    BASE_MAIN_URL = f"https://www.{MAIN_DOMAIN}"
    # This API key can be hardcoded because it appears to never change. It was
    # originally extracted from app.js on the website.
    API_KEY = "857a1e5d-e35e-4fdf-805b-a87b6f8364bf"

    def __init__(
        self,
        get_around_client: GetAround | None = None,
        timezone: str = "America/Los_Angeles",
    ) -> None:
        """Initialize the DivingBoard client."""
        self.timezone = timezone
        self.get_around_client = get_around_client or GetAround()

        self._authentication_token_value = ""
        self._realm_value = ""

        self.vod = Vod(self)
        self.season = Season(self)
        self.schedule = Schedule(self)
        self.adjacent_series_to = SeriesAdjacentTo(self)
        self.search = Search(self)
        self.series = Series(self)

        super().__init__()

    def __fetch_auth_values(self) -> None:
        """Downloads and caches the authorisation token and realm."""
        url = (
            f"{BASE_API_URL}/api/v1/init/"
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
        headers = {
            "User-Agent": USER_AGENT,
            "Origin": self.BASE_MAIN_URL,
            "Referer": f"{self.BASE_MAIN_URL}/",
            "x-api-key": self.API_KEY,
        }
        operation = "init (Authentication)"
        logger.debug("Downloading: %s", operation)
        start = time.monotonic()
        response = self.get_around_client.get(url, headers=headers)
        logger.debug("Downloaded %s (%.4f s)", operation, time.monotonic() - start)
        json_response = response.json()
        self._realm_value = json_response["settings"]["realm"]
        authentication = json_response["authentication"]
        self._authentication_token_value = authentication["authorisationToken"]
        # Although authentication has a refreshToken value there is no designated
        # expiration date in the returned data, and testing has shown that authorisation
        # tokens may not actually expire.

    @property
    def _authentication_token(self) -> str:
        if not self._authentication_token_value:
            self.__fetch_auth_values()

        return self._authentication_token_value

    @_authentication_token.setter
    def _authentication_token(self, value: str) -> None:
        self._authentication_token_value = value

    @property
    def _realm(self) -> str:
        if not self._realm_value:
            self.__fetch_auth_values()

        return self._realm_value

    @_realm.setter
    def _realm(self, value: str) -> None:
        self._realm_value = value

    def download(
        self,
        url: str,
        params: dict[str, Any],
        log_id: str,
    ) -> dict[str, Any]:
        """Downloads from the API."""
        headers = {
            "User-Agent": USER_AGENT,
            "authorization": f"Bearer {self._authentication_token}",
            "x-api-key": self.API_KEY,
            "Origin": self.BASE_MAIN_URL,
            "Referer": f"{self.BASE_MAIN_URL}/",
            "Realm": self._realm,
        }

        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.get(url=url, headers=headers, params=params)

        if response.is_success:
            logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
            return response.json()

        msg = f"Unexpected response status code: {response.status_code}"
        raise HTTPError(msg)
