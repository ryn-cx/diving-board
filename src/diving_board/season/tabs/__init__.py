"""Season tabs extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.tabs.model import SeasonTabsModel


class SeasonTabs(BaseExtractor[SeasonTabsModel]):
    """Extracts data from Season where field_type=tabs."""

    _response_model = SeasonTabsModel
