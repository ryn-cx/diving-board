"""Vod bucket extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.bucket.model import VodBucketModel


class VodBucket(BaseExtractor[VodBucketModel]):
    """Extracts data from Vod where field_type=bucket."""

    _response_model = VodBucketModel
