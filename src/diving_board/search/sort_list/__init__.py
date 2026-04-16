"""Search sort list extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.search.sort_list.model import SearchSortListModel


class SearchSortList(BaseExtractor[SearchSortListModel]):
    """Extracts data from Search where field_type=sortList."""

    _response_model = SearchSortListModel
