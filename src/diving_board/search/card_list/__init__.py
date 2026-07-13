"""Contains the SearchCardList class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.search.card_list.models import SearchCardListModel


class SearchCardList(BaseExtractor[SearchCardListModel]):
    """Extract the card list element from Search."""

    _response_model = SearchCardListModel
