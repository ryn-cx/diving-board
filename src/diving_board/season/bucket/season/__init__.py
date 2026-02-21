"""Season bucket (season type) extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.bucket.season.model import SeasonBucketSeasonModel


class SeasonBucketSeason(BaseExtractor[SeasonBucketSeasonModel]):
    """Extracts data from Season where field_type=bucket and type=season."""

    _response_model = SeasonBucketSeasonModel
