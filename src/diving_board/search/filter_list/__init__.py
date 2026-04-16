"""Search filter list extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.search.filter_list.model import SearchFilterListModel


class SearchFilterList(BaseExtractor[SearchFilterListModel]):
    """Extracts data from Search where field_type=filterList."""

    _response_model = SearchFilterListModel
