"""Playlist hero extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.playlist.hero.model import PlaylistHeroModel


class PlaylistHero(BaseExtractor[PlaylistHeroModel]):
    """Extracts data from Playlist where field_type=hero."""

    _response_model = PlaylistHeroModel
