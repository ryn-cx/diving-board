"""Season series extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.series.model import SeasonSeriesModel


class SeasonSeries(BaseExtractor[SeasonSeriesModel]):
    """Provides methods to manage the series element from season data."""

    @cached_property
    @override
    def _response_model(self) -> type[SeasonSeriesModel]:
        return SeasonSeriesModel
