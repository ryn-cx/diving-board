"""Season text block extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.text_block.model import SeasonTextBlockModel


class SeasonTextBlock(BaseExtractor[SeasonTextBlockModel]):
    """Extracts data from Season where field_type=textBlock."""

    _response_model = SeasonTextBlockModel
