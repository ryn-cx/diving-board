"""Search API endpoint."""

from __future__ import annotations

from typing import Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.search.models import SearchModel


class Search(BaseEndpoint[SearchModel]):
    """Provides methods to download, parse, and retrieve search data."""

    SEARCH_API_URL = "https://search.dce-prod.dicelaboratory.com"

    _response_model = SearchModel

    def download(self, query: str, timezone: str = "") -> dict[str, Any]:
        """Downloads search data for a given query.

        Args:
            query: The search query string.
            timezone: The timezone to use for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        endpoint = "search"
        params: dict[str, str | int] = {
            "query": query,
            "timezone": timezone or self._client.timezone,
        }
        return self._client.download(endpoint, params, base_url=self.SEARCH_API_URL)

    def get(self, query: str, timezone: str = "") -> SearchModel:
        """Downloads and parses search data for a given query.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            query: The search query string.
            timezone: The timezone to use for the request.

        Returns:
            A SearchModel containing the parsed data.
        """
        response = self.download(query, timezone)
        return self.parse(response)
