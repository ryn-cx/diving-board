"""Contains the SearchFilterList class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.search.filter_list.model import SearchFilterListModel


class SearchFilterList(BaseExtractor[SearchFilterListModel]):
    """Extract the filter list element from Search."""

    _response_model = SearchFilterListModel
