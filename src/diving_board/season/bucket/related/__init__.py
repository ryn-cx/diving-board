"""Contains the SeasonBucketRelated class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.bucket.related.models import SeasonBucketRelatedModel


class SeasonBucketRelated(BaseExtractor[SeasonBucketRelatedModel]):
    """Extract the related-type bucket element from Season."""

    _response_model = SeasonBucketRelatedModel
