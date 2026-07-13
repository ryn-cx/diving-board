# TODO: Validate
"""Contains the SeasonTabs class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.tabs.models import SeasonTabsModel


class SeasonTabs(BaseExtractor[SeasonTabsModel]):
    """Extract the tabs element from Season."""

    _response_model = SeasonTabsModel
