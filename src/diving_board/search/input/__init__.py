# TODO: Validate
"""Contains the SearchInput class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.search.input.models import SearchInputModel


class SearchInput(BaseExtractor[SearchInputModel]):
    """Extract the search input element from Search."""

    _response_model = SearchInputModel
