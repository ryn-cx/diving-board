"""Contains the SeriesAdjacentTo class."""

from __future__ import annotations

from typing import Any

from diving_board.adjacent_series.models import AdjacentSeries as AdjacentSeriesModel
from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL


class SeriesAdjacentTo(BaseEndpoint[AdjacentSeriesModel]):
    """Manage the series adjacent to file."""

    _response_model = AdjacentSeriesModel

    def download(self, series_id: int, season_id: int) -> dict[str, Any]:
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
            f"{BASE_API_URL}/api/v4/series/{series_id}/adjacentTo/{season_id}",
            {"size": 25},
            f"{self.__class__.__name__} {series_id}/{season_id}",
        )

    def get(self, series_id: int, season_id: int) -> AdjacentSeriesModel:
        """Downloads and parses the series adjacent to file.

        Raises:
            HTTPError: If series_id or season_id is invalid.
        """
        response = self.download(series_id=series_id, season_id=season_id)
        return self.parse(response)
