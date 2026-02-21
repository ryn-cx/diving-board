"""DivingBoard is a client for downloading and parsing data from HiDive."""

import re
from datetime import datetime
from functools import cached_property
from logging import NullHandler, getLogger
from typing import Any

import requests

from diving_board.adjacent_series import AdjacentSeries
from diving_board.exceptions import HTTPError
from diving_board.playlist import Playlist
from diving_board.schedule import Schedule
from diving_board.schedule import ScheduleGroupList as ScheduleGroupList
from diving_board.season import Season
from diving_board.vod import Vod

logger = getLogger(__name__)
logger.addHandler(NullHandler())

USER_AGENT = (
    "Mozilla/5.0 (Linux; Android 10; K) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/134.0.0.0 Mobile Safari/537.3"
)


class DivingBoard:
    """Interface for downloading and parsing data from HiDive."""

    MAIN_DOMAIN = "hidive.com"
    BASE_MAIN_URL = f"https://www.{MAIN_DOMAIN}"
    API_DOMAIN = "dce-frontoffice.imggaming.com"
    BASE_API_URL = f"https://{API_DOMAIN}"

    def __init__(
        self,
        timezone: str = "America/Los_Angeles",
        timeout: int = 30,
    ) -> None:
        """Initialize the DivingBoard client."""
        self.timezone = timezone
        self.timeout = timeout

        self.__auth_token_value = ""
        self.__realm_value = ""

        self.playlist = Playlist(self)
        self.vod = Vod(self)
        self.season = Season(self)
        self.schedule = Schedule(self)
        self.adjacent_series = AdjacentSeries(self)

        super().__init__()

    @cached_property
    def __api_key(self) -> str:
        """Returns the API key.

        Downloads and caches the API key from app.js.
        """
        # This API key can be hardcoded because it appears to never change. Below this
        # is the original code to extract it (not available in Git history because this
        # is before the initial commit).
        return "857a1e5d-e35e-4fdf-805b-a87b6f8364bf"

        # Example request headers:
        """GET /code/js/app.43221e881b6a9a9bc6fe.js HTTP/3
        Host: www.hidive.com
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0)
                    Gecko/20100101 Firefox/147.0
        Accept: */*
        Accept-Language: en-US,en;q=0.9
        Accept-Encoding: gzip, deflate, br, zstd
        Sec-GPC: 1
        Connection: keep-alive
        Referer: https://www.hidive.com/browse
        Sec-Fetch-Dest: script
        Sec-Fetch-Mode: no-cors
        Sec-Fetch-Site: same-origin
        TE: trailers"""

        # This URL is hard coded, but the URL changes sometimes, however though the old
        # version of the URL will continue to work. So far hard coding the URL has had
        # no negative consequences, but in the future it may be necessary to obtain the
        # URL dynamically. For now, hardcoding the URL is considered to be the superior
        # option because it means there will be one less network request needed to
        # initialize the client.
        # The URL was obtained from the network requests made when visiting any page but
        # the homepage. For example: https://www.hidive.com/browse
        app_js_file_name = "app.43221e881b6a9a9bc6fe.js"
        url = f"{self.BASE_MAIN_URL}/code/js/{app_js_file_name}"
        logger.info("Downloading API key: %s", url)
        headers = {
            "User-Agent": USER_AGENT,
            # This URL is not returned on the homepage so set the referer to a commonly
            # used page that actually returns the URL.
            "Referer": f"{self.BASE_MAIN_URL}/browse",
        }
        response = requests.get(url, headers=headers, timeout=self.timeout)
        response_text = response.text

        if not (match := re.search(r'API_KEY:"([0-9a-f-]+)"', response_text)):
            msg = f"Failed to extract API key from {app_js_file_name}"
            raise ValueError(msg)

        return match.group(1)

    def __download_auth_values(self) -> None:
        """Downloads and caches the authorisation token and realm."""
        # Example request headers:
        """GET /api/v1/init/
                            ?lk=language
                            &pk=subTitleLanguage
                            &pk=subtitlePreferenceMode
                            &pk=audioLanguage
                            &pk=autoAdvance
                            &pk=pluginAccessTokens
                            &pk=videoBackgroundAutoPlay
                            &readLicences=true
                            &countEvents=LIVE
                            &menuTargetPlatform=WEB
                            &readIconStore=ENABLED
                            &readUserProfiles=true
                            &section=browse
                            &geoBlockedContentDisplayMode=SHOW
                            &displaySectionLinkBuckets=SHOW
                            &displayEpgBuckets=HIDE
                            &displayContentAvailableOnSignIn=SHOW
                            &rpp=12&bpp=4&bspp=10 HTTP/2
        Host: dce-frontoffice.imggaming.com
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0)
                    Gecko/20100101 Firefox/147.0
        Accept: application/json, text/plain, */*
        Accept-Language: en-US
        Accept-Encoding: gzip, deflate, br, zstd
        Referer: https://www.hidive.com/
        Content-Type: application/json
        x-api-key: 857a1e5d-e35e-4fdf-805b-a87b6f8364bf
        app: dice
        x-app-var: 6.60.0.b702efb
        Origin: https://www.hidive.com
        Sec-GPC: 1
        Connection: keep-alive
        Sec-Fetch-Dest: empty
        Sec-Fetch-Mode: cors
        Sec-Fetch-Site: cross-site
        Priority: u=4
        TE: trailers"""

        url = (
            f"{self.BASE_API_URL}/api/v1/init/"
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
        logger.info("Downloading authorisation token: %s", url)

        headers = {
            "User-Agent": USER_AGENT,
            "Origin": self.BASE_MAIN_URL,
            "Referer": f"{self.BASE_MAIN_URL}/",
            "x-api-key": self.__api_key,
        }
        response = requests.get(url, headers=headers, timeout=self.timeout)
        json_response = response.json()
        self.__realm_value = json_response["settings"]["realm"]
        authentication = json_response["authentication"]
        self.__auth_token_value = authentication["authorisationToken"]
        # Although authentication has a refreshToken value there is no designated
        # expiration date in the returned data, and testing has shown that authorisation
        # tokens may not actually expire.

    @property
    def __auth_token(self) -> str:
        if not self.__auth_token_value:
            self.__download_auth_values()

        return self.__auth_token_value

    @__auth_token.setter
    def __auth_token(self, value: str) -> None:
        self.__auth_token_value = value

    @property
    def __realm(self) -> str:
        if not self.__realm_value:
            self.__download_auth_values()

        return self.__realm_value

    @__realm.setter
    def __realm(self, value: str) -> None:
        self.__realm_value = value

    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
    ) -> dict[str, Any]:
        """Downloads data from the API for a given endpoint and parameters."""
        headers = {
            "User-Agent": USER_AGENT,
            "authorization": f"Bearer {self.__auth_token}",
            "x-api-key": self.__api_key,
            "Origin": self.BASE_MAIN_URL,
            "Referer": f"{self.BASE_MAIN_URL}/",
            "Realm": self.__realm,
        }

        url = f"{self.BASE_API_URL}/{endpoint}"

        request = requests.Request("GET", url, params=params)
        prepared = request.prepare()
        logger.info("Downloading API data: %s", prepared.url)
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=self.timeout,
        )

        # PLR2004 - 200 represents the status code "200 OK".
        if response.status_code != 200:  # noqa: PLR2004
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        output = response.json()
        output["diving_board"] = {}
        output["diving_board"]["url"] = url
        output["diving_board"]["timestamp"] = datetime.now().astimezone().isoformat()
        headers.pop("authorization")
        output["diving_board"]["headers"] = headers
        output["diving_board"]["params"] = params

        return output
