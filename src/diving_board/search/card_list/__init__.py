"""Search card list extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.search.card_list.model import SearchCardListModel


class SearchCardList(BaseExtractor[SearchCardListModel]):
    """Extracts data from Search where field_type=cardList."""

    _response_model = SearchCardListModel
