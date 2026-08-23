# TODO: Validate
"""Contains the DivingBoard class."""

from __future__ import annotations

from http import HTTPStatus
from logging import NullHandler, getLogger
from time import monotonic
from typing import Any

from get_around import GetAround

from diving_board.adjacent_series import AdjacentSeries
from diving_board.constants import BASE_API_URL
from diving_board.exceptions import HTTPError, ResourceNotFoundError
from diving_board.schedule import Schedule
from diving_board.search import Search
from diving_board.season import Season
from diving_board.series import Series
from diving_board.vod import Vod

logger = getLogger(__name__)
logger.addHandler(NullHandler())

MAIN_URL = "https://www.hidive.com"

USER_AGENT = (
    "Mozilla/5.0 (Linux; Android 10; K) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/134.0.0.0 Mobile Safari/537.3"
)

# This API key can be hardcoded because it appears to never change. It was
# originally extracted from app.js on the website.
API_KEY = "857a1e5d-e35e-4fdf-805b-a87b6f8364bf"


# TODO: Validate
class DivingBoard:
    """HiDive API wrapper."""

    # TODO: Validate
    def __init__(
        self,
        get_around_client: GetAround | None = None,
        timezone: str = "America/Los_Angeles",
    ) -> None:
        """Initialize the DivingBoard client.

        The client holds one attribute per endpoint, so `client.vod(vod_id)`
        looks a video up and `client.vod.download(vod_id)` and
        `client.vod.load(data)` are the halves of it.
        """
        self.timezone = timezone
        self.get_around_client = get_around_client or GetAround()

        self._authentication_token_value = ""
        self._realm_value = ""

        self.vod = Vod(self)
        self.season = Season(self)
        self.schedule = Schedule(self)
        self.adjacent_series = AdjacentSeries(self)
        self.search = Search(self)
        self.series = Series(self)

    # TODO: Validate
    def _download_auth_values(self) -> None:
        """Download the authorisation token and the realm and keep them."""
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
        logger.debug("Downloading token:")
        start = monotonic()
        response = self.get_around_client.get(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Origin": MAIN_URL,
                "Referer": f"{MAIN_URL}/",
                "x-api-key": API_KEY,
            },
        )
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded token (%.4f s)", monotonic() - start)

        parsed = response.json()
        self._realm_value = parsed["settings"]["realm"]
        # The authentication holds a refreshToken as well, but nothing says when
        # the authorisation token expires and testing has shown that it does not.
        self._authentication_token_value = parsed["authentication"][
            "authorisationToken"
        ]

    # TODO: Validate
    @property
    def _authentication_token(self) -> str:
        if not self._authentication_token_value:
            self._download_auth_values()
        return self._authentication_token_value

    # TODO: Validate
    @property
    def _realm(self) -> str:
        if not self._realm_value:
            self._download_auth_values()
        return self._realm_value

    # TODO: Validate
    def download(
        self,
        url: str,
        params: dict[str, Any],
        log_id: str,
    ) -> str:
        """Download from the API and return the body as it was served.

        Raises:
            ResourceNotFoundError: If the API says the thing does not exist.
            HTTPError: If the request is answered with anything else but a 200.
        """
        headers = {
            "User-Agent": USER_AGENT,
            "authorization": f"Bearer {self._authentication_token}",
            "x-api-key": API_KEY,
            "Origin": MAIN_URL,
            "Referer": f"{MAIN_URL}/",
            "Realm": self._realm,
        }

        logger.debug("Downloading: %s", log_id)
        start = monotonic()
        response = self.get_around_client.get(url, headers=headers, params=params)

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise ResourceNotFoundError(response.status_code, response.text)
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)
        return response.text
