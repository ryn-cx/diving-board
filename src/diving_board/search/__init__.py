"""Search API endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.search.card_list import SearchCardList
from diving_board.search.filter_list import SearchFilterList
from diving_board.search.input import SearchInput
from diving_board.search.models import SearchModel
from diving_board.search.sort_list import SearchSortList

if TYPE_CHECKING:
    from diving_board.search.card_list.model import SearchCardListModel
    from diving_board.search.filter_list.model import SearchFilterListModel
    from diving_board.search.input.model import SearchInputModel
    from diving_board.search.sort_list.model import SearchSortListModel


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

    def extract_input(
        self,
        data: SearchModel,
        *,
        update_model: bool = True,
    ) -> SearchInputModel:
        """Extract the search input element from search data.

        Args:
            data: Search data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SearchInputModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "search",
            SearchInput,
            update_model=update_model,
        )

    def extract_filter_list(
        self,
        data: SearchModel,
        *,
        update_model: bool = True,
    ) -> SearchFilterListModel:
        """Extract the filter list element from search data.

        Args:
            data: Search data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SearchFilterListModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "filterList",
            SearchFilterList,
            update_model=update_model,
        )

    def extract_sort_list(
        self,
        data: SearchModel,
        *,
        update_model: bool = True,
    ) -> SearchSortListModel:
        """Extract the sort list element from search data.

        Args:
            data: Search data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SearchSortListModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "sortList",
            SearchSortList,
            update_model=update_model,
        )

    def extract_card_list(
        self,
        data: SearchModel,
        *,
        update_model: bool = True,
    ) -> SearchCardListModel:
        """Extract the card list element from search data.

        Args:
            data: Search data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SearchCardListModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "cardList",
            SearchCardList,
            update_model=update_model,
        )
