"""Contains the SeasonSeries class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.series.models import SeasonSeriesModel


class SeasonSeries(BaseExtractor[SeasonSeriesModel]):
    """Extract the series element from Season."""

    _response_model = SeasonSeriesModel
