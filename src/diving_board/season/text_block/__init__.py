"""Season text block extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.text_block.model import SeasonTextBlockModel


class SeasonTextBlock(BaseExtractor[SeasonTextBlockModel]):
    """Provides methods to manage the text block element from season data."""

    @cached_property
    @override
    def _response_model(self) -> type[SeasonTextBlockModel]:
        return SeasonTextBlockModel
