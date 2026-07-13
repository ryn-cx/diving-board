"""Contains the Series class."""

from __future__ import annotations

from typing import Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL
from diving_board.series.models import SeriesModel


class Series(BaseEndpoint[SeriesModel]):
    """Manage the series file.

    Raises:
        HTTPError: If series_id is invalid.

    Example request: https://www.hidive.com/series/2311
        OPTIONS /api/v1/view?type=series&id=4083&timezone=America%2FLos_Angeles HTTP/2
        Host: dce-frontoffice.imggaming.com
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
        Accept: */*
        Accept-Language: en-US,en;q=0.9
        Accept-Encoding: gzip, deflate, br, zstd
        Access-Control-Request-Method: GET
        Access-Control-Request-Headers: app,authorization,content-type,realm,x-api-key,x-app-var
        Referer: https://www.hidive.com/
        Origin: https://www.hidive.com
        Connection: keep-alive
        Sec-Fetch-Dest: empty
        Sec-Fetch-Mode: cors
        Sec-Fetch-Site: cross-site
        Priority: u=4
        TE: trailers
    """

    _response_model = SeriesModel

    def download(
        self,
        series_id: int | str,
        timezone: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the series file.

        Raises:
            HTTPError: If series_id is invalid.
        """
        return self._client.download(
            f"{BASE_API_URL}/api/v1/view",
            {
                "type": "series",
                "id": int(series_id),
                "timezone": timezone or self._client.timezone,
            },
            f"{self.__class__.__name__} {series_id}",
        )

    def get(self, series_id: int | str, timezone: str | None = None) -> SeriesModel:
        """Downloads and parses the series file."""
        response = self.download(series_id, timezone)
        return self.parse(response)
