"""Season tabs extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.tabs.model import SeasonTabsModel


class SeasonTabs(BaseExtractor[SeasonTabsModel]):
    """Provides methods to manage the tabs element from season data."""

    @cached_property
    @override
    def _response_model(self) -> type[SeasonTabsModel]:
        return SeasonTabsModel
