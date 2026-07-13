# TODO: Validate
"""Contains the VodTextBlock class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.text_block.models import VodTextBlockModel


class VodTextBlock(BaseExtractor[VodTextBlockModel]):
    """Extract the text block element from Vod."""

    _response_model = VodTextBlockModel
