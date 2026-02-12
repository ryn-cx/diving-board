"""Playlist hero extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.playlist.hero.model import PlaylistHeroModel


class PlaylistHero(BaseExtractor[PlaylistHeroModel]):
    """Provides methods to manage the hero element from playlist data."""

    @cached_property
    @override
    def _response_model(self) -> type[PlaylistHeroModel]:
        return PlaylistHeroModel
