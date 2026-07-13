# TODO: Validate
"""Contains the VodTabs class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.tabs.models import VodTabsModel


class VodTabs(BaseExtractor[VodTabsModel]):
    """Extract the tabs element from Vod."""

    _response_model = VodTabsModel
