"""Vod text block extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.text_block.model import VodTextBlockModel


class VodTextBlock(BaseExtractor[VodTextBlockModel]):
    """Extracts data from Vod where field_type=textBlock."""

    _response_model = VodTextBlockModel
