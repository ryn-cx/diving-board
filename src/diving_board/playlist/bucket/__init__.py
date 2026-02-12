"""Playlist bucket extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.playlist.bucket.model import PlaylistBucketModel


class PlaylistBucket(BaseExtractor[PlaylistBucketModel]):
    """Provides methods to manage bucket elements from playlist data."""

    @cached_property
    @override
    def _response_model(self) -> type[PlaylistBucketModel]:
        return PlaylistBucketModel
