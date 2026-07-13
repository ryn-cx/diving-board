"""Contains the SeasonTextBlock class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.text_block.models import SeasonTextBlockModel


class SeasonTextBlock(BaseExtractor[SeasonTextBlockModel]):
    """Extract the text block element from Season."""

    _response_model = SeasonTextBlockModel
