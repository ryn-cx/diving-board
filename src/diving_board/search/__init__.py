# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.search.card_list import SearchCardList
from diving_board.search.input import SearchInput
from diving_board.search.models import SearchModel

if TYPE_CHECKING:
    from diving_board.search.card_list.models import SearchCardListModel
    from diving_board.search.input.models import SearchInputModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Search(BaseEndpoint[SearchModel]):
    """Manage the search file."""

    _response_model = SearchModel

    def get_log_id(self, query: str, timezone: str | None = None) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {query=}",
            timezone=(timezone, None),
        )

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
            self.get_log_id(query, timezone),
        )

    def download_and_parse(
        self,
        query: str,
        timezone: str | None = None,
    ) -> SearchModel:
        """Downloads and parses the search file."""
        return self.parse(self.download(query, timezone))

    def extract_search(
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
