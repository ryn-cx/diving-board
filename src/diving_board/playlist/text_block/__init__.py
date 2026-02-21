"""Playlist text block extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.playlist.text_block.model import PlaylistTextBlockModel


class PlaylistTextBlock(BaseExtractor[PlaylistTextBlockModel]):
    """Extracts data from Playlist where field_type=textBlock."""

    _response_model = PlaylistTextBlockModel
