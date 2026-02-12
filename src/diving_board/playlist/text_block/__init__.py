"""Playlist text block extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.playlist.text_block.model import PlaylistTextBlockModel


class PlaylistTextBlock(BaseExtractor[PlaylistTextBlockModel]):
    """Provides methods to manage the text block element from playlist data."""

    @cached_property
    @override
    def _response_model(self) -> type[PlaylistTextBlockModel]:
        return PlaylistTextBlockModel
