"""Adjacent Series endpoint."""

from __future__ import annotations

from typing import Any

from diving_board.adjacent_series.models import AdjacentSeries as AdjacentSeriesModel
from diving_board.base_api_endpoint import BaseEndpoint


class AdjacentSeries(BaseEndpoint[AdjacentSeriesModel]):
    """Provides methods to download, parse, and retrieve adjacent series data."""

    _response_model = AdjacentSeriesModel

    def download(
        self,
        series_id: int,
        season_id: int,
        size: int = 25,
    ) -> dict[str, Any]:
        """Downloads adjacent series data for a given series and season.

        Args:
            series_id: The ID of the series to get adjacent series for.
            season_id: The ID of the season to get adjacent series for.
            size: The number of adjacent series to return.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        # Example request headers from https://www.hidive.com/season/34391
        """GET /api/v4/series/1049/adjacentTo/34391?size=25 HTTP/2
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
        Realm: dce.hidive
        x-app-var: 6.60.0.b702efb
        Authorization: Bearer TOKEN
        Origin: https://www.hidive.com
        Sec-GPC: 1
        Connection: keep-alive
        Sec-Fetch-Dest: empty
        Sec-Fetch-Mode: cors
        Sec-Fetch-Site: cross-site
        Priority: u=4
        TE: trailers"""

        endpoint = f"api/v4/series/{series_id}/adjacentTo/{season_id}"
        params = {"size": size}
        return self._client.download(endpoint, params)

    def get(
        self,
        series_id: int,
        season_id: int,
        size: int = 25,
    ) -> AdjacentSeriesModel:
        """Downloads and parses adjacent series data for a given series and season.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            series_id: The ID of the series to get adjacent series for.
            season_id: The ID of the season to get adjacent series for.
            size: The number of adjacent series to return.

        Returns:
            An AdjacentSeries model containing the parsed data.
        """
        response = self.download(
            series_id=series_id,
            season_id=season_id,
            size=size,
        )
        return self.parse(response)
