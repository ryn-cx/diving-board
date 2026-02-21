"""Season series extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.series.model import SeasonSeriesModel


class SeasonSeries(BaseExtractor[SeasonSeriesModel]):
    """Extracts data from Season where field_type=series."""

    _response_model = SeasonSeriesModel
