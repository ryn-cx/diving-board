"""Contains the SeasonBucketSeason class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.bucket.season.models import SeasonBucketSeasonModel


class SeasonBucketSeason(BaseExtractor[SeasonBucketSeasonModel]):
    """Extract the season-type bucket element from Season."""

    _response_model = SeasonBucketSeasonModel
