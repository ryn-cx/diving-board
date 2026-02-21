"""Playlist bucket related extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.playlist.bucket.related.model import PlaylistBucketRelatedModel


class PlaylistBucketRelated(BaseExtractor[PlaylistBucketRelatedModel]):
    """Extracts data from Playlist where field_type=bucket and type=related."""

    _response_model = PlaylistBucketRelatedModel
