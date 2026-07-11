# TODO: Validate
"""Adjacent Series endpoint."""

from __future__ import annotations

from typing import Any, override

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
        # Request from: https://www.hidive.com/season/34391
        endpoint = f"api/v4/series/{series_id}/adjacentTo/{season_id}"
        params = {"size": size}
        return self._client.download(endpoint, params)

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        # An unknown series/season still returns 200 with both adjacency lists
        # empty, so treat "no preceding and no following seasons" as no content.
        return bool(response["followingSeasons"] or response["precedingSeasons"])

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

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        response = self.download(
            series_id=series_id,
            season_id=season_id,
            size=size,
        )
        return self._parse_or_raise(response, has_content=self.has_content(response))
