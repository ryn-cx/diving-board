"""Contains the Search class."""

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
    """Manage the search file."""

    _response_model = SearchModel

    def download(self, query: str, timezone: str | None = None) -> dict[str, Any]:
        """Downloads the search file.

        Example request: https://www.hidive.com/search
            OPTIONS /search?query=2.5&timezone=America%2FLos_Angeles HTTP/2
            Host: search.dce-prod.dicelaboratory.com
            User-Agent: __REDACTED__
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
        return self._client.download(
            "https://search.dce-prod.dicelaboratory.com/search",
            {
                "query": query,
                "timezone": timezone or self._client.timezone,
            },
            f"{self.__class__.__name__} {query}",
        )

    def get(self, query: str, timezone: str | None = None) -> SearchModel:
        """Downloads and parses the search file."""
        response = self.download(query, timezone)
        return self.parse(response)

    def extract_input(
        self,
        data: SearchModel,
        *,
        update_model: bool = True,
    ) -> SearchInputModel:
        """Extract the search input element from Search."""
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
        """Extract the filter list element from Search."""
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
        """Extract the sort list element from Search."""
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
        """Extract the card list element from Search."""
        return self._extract_element(
            data.elements,
            "cardList",
            SearchCardList,
            update_model=update_model,
        )
