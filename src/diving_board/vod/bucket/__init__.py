# TODO: Validate
"""Contains the VodBucket class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.bucket.model import VodBucketModel


class VodBucket(BaseExtractor[VodBucketModel]):
    """Extract the bucket element from Vod."""

    _response_model = VodBucketModel
