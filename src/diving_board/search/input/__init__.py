"""Search input extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.search.input.model import SearchInputModel


class SearchInput(BaseExtractor[SearchInputModel]):
    """Extracts data from Search where field_type=search."""

    _response_model = SearchInputModel
