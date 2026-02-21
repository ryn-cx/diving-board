"""Vod tabs extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.tabs.model import VodTabsModel


class VodTabs(BaseExtractor[VodTabsModel]):
    """Extracts data from Vod where field_type=tabs."""

    _response_model = VodTabsModel
