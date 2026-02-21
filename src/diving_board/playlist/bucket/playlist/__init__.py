"""Playlist bucket playlist extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.playlist.bucket.playlist.model import PlaylistBucketPlaylistModel


class PlaylistBucketPlaylist(BaseExtractor[PlaylistBucketPlaylistModel]):
    """Extracts data from PlaylistBucket where field_type=bucket and type=playlist."""

    _response_model = PlaylistBucketPlaylistModel
