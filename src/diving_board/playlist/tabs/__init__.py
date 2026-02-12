"""Playlist tabs extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.playlist.tabs.model import PlaylistTabsModel


class PlaylistTabs(BaseExtractor[PlaylistTabsModel]):
    """Provides methods to manage the tabs element from playlist data."""

    @cached_property
    @override
    def _response_model(self) -> type[PlaylistTabsModel]:
        return PlaylistTabsModel
