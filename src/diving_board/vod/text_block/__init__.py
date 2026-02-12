"""Vod text block extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.text_block.model import VodTextBlockModel


class VodTextBlock(BaseExtractor[VodTextBlockModel]):
    """Provides methods to manage the text block element from vod data."""

    @cached_property
    @override
    def _response_model(self) -> type[VodTextBlockModel]:
        return VodTextBlockModel
