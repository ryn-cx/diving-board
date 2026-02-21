"""Season bucket (related type) extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.bucket.related.model import SeasonBucketRelatedModel


class SeasonBucketRelated(BaseExtractor[SeasonBucketRelatedModel]):
    """Extracts data from Season where field_type=bucket and type=related."""

    _response_model = SeasonBucketRelatedModel
