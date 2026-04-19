"""Series API endpoint."""

from __future__ import annotations

from typing import Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.series.models import SeriesModel


class Series(BaseEndpoint[SeriesModel]):
    """Provides methods to download, parse, and retrieve series data."""

    _response_model = SeriesModel

    def download(self, series_id: int, timezone: str = "") -> dict[str, Any]:
        """Downloads series data for a given series ID.

        Args:
            series_id: The ID of the series to download.
            timezone: The timezone to use for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        # Request from: https://www.hidive.com/series/1091
        endpoint = "api/v1/view"
        params: dict[str, str | int] = {
            "type": "series",
            "id": series_id,
            "timezone": timezone or self._client.timezone,
        }
        return self._client.download(endpoint, params)

    def get(self, series_id: int, timezone: str = "") -> SeriesModel:
        """Downloads and parses series data for a given series ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            series_id: The ID of the series to get.
            timezone: The timezone to use for the request.

        Returns:
            A SeriesModel containing the parsed data.
        """
        response = self.download(series_id, timezone)
        return self.parse(response)
