# TODO: Validate
"""Contains the SeriesAdjacentTo class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from diving_board.adjacent_series.models import SeriesAdjacentToModel
from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class SeriesAdjacentTo(BaseEndpoint[SeriesAdjacentToModel]):
    """Manage the series adjacent to file."""

    _response_model = SeriesAdjacentToModel

    def get_log_id(self, series_id: int | str, season_id: int | str) -> str:
        """Build the log id for a download."""
        return f"{self.__class__.__name__} {series_id=} {season_id=}"

    def download(self, series_id: int | str, season_id: int | str) -> dict[str, Any]:
        """Downloads the series adjacent to file.

        Raises:
            HTTPError: If series_id or season_id is invalid.

        Example request: https://www.hidive.com/season/18908
            GET /api/v4/series/1019/adjacentTo/18908?size=25 HTTP/2
            Host: dce-frontoffice.imggaming.com
            User-Agent: __REDACTED__
            Accept: application/json, text/plain, */*
            Accept-Language: en-US
            Accept-Encoding: gzip, deflate, br, zstd
            Referer: https://www.hidive.com/
            Content-Type: application/json
            x-api-key: 857a1e5d-e35e-4fdf-805b-a87b6f8364bf (This is a public value)
            app: dice
            Realm: dce.hidive
            x-app-var: 6.60.0.5aaf921
            Authorization: Bearer __REDACTED__
            Origin: https://www.hidive.com
            Connection: keep-alive
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: cross-site
        """
        return self._client.download(
            f"{BASE_API_URL}/api/v4/series/{int(series_id)}/adjacentTo/{int(season_id)}",
            {"size": 25},
            self.get_log_id(series_id, season_id),
        )

    def download_and_parse(
        self,
        series_id: int | str,
        season_id: int | str,
    ) -> SeriesAdjacentToModel:
        """Downloads and parses the series adjacent to file.

        Raises:
            HTTPError: If series_id or season_id is invalid.
        """
        return self.parse(self.download(series_id, season_id))
