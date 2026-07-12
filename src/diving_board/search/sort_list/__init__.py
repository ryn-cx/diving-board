"""Contains the SearchSortList class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.search.sort_list.model import SearchSortListModel


class SearchSortList(BaseExtractor[SearchSortListModel]):
    """Extract the sort list element from Search."""

    _response_model = SearchSortListModel
