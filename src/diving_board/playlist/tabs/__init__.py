"""Playlist tabs extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.playlist.tabs.model import PlaylistTabsModel


class PlaylistTabs(BaseExtractor[PlaylistTabsModel]):
    """Extracts data from Playlist where field_type=tabs."""

    _response_model = PlaylistTabsModel
