"""Vod bucket extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.bucket.model import VodBucketModel


class VodBucket(BaseExtractor[VodBucketModel]):
    """Provides methods to manage bucket elements from vod data."""

    @cached_property
    @override
    def _response_model(self) -> type[VodBucketModel]:
        return VodBucketModel
