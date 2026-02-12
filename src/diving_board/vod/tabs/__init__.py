"""Vod tabs extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.tabs.model import VodTabsModel


class VodTabs(BaseExtractor[VodTabsModel]):
    """Provides methods to manage the tabs element from vod data."""

    @cached_property
    @override
    def _response_model(self) -> type[VodTabsModel]:
        return VodTabsModel
