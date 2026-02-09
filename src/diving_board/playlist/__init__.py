"""Playlist API endpoint."""

from __future__ import annotations

from functools import cached_property
from typing import Any, override

from diving_board.base_api_endpoint import BaseEndpoint, BaseExtractor
from diving_board.playlist import models
from diving_board.playlist.bucket_playlist import models as bucket_playlist_models


class Playlist(BaseEndpoint[models.Playlist]):
    """Provides methods to download, parse, and retrieve playlist data.

    Interacts with the playlist API endpoint.
    """

    @cached_property
    @override
    def _response_model(self) -> type[models.Playlist]:
        """Return the Pydantic model class for this client."""
        return models.Playlist

    def download(self, playlist_id: int) -> dict[str, Any]:
        """Downloads playlist data for a given playlist ID.

        Args:
            playlist_id: The ID of the playlist to download.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        # Example request headers from https://www.hidive.com/playlist/19078
        """GET /api/v1/view?type=playlist&id=19078&timezone=America%2FLos_Angeles HTTP/2
            Host: dce-frontoffice.imggaming.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0)
                        Gecko/20100101 Firefox/147.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US
            Accept-Encoding: gzip, deflate, br, zstd
            Referer: https://www.hidive.com/
            Content-Type: application/json
            x-api-key: 857a1e5d-e35e-4fdf-805b-a87b6f8364bf
            app: dice
            Realm: dce.hidive
            x-app-var: 6.60.0.ae5c96d
            Authorization: Bearer TOKEN
            Origin: https://www.hidive.com
            Connection: keep-alive
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: cross-site
            Priority: u=4"""
        endpoint = "api/v1/view"
        params: dict[str, str | int] = {
            "type": "playlist",
            "id": playlist_id,
            "timezone": self._client.timezone,
        }
        return self._client.download_api_request(endpoint, params)

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> models.Playlist:
        """Parses playlist data into a Playlist model.

        Args:
            data: The playlist data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A Playlist model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return models.Playlist.model_validate(data)

    def get(self, playlist_id: int) -> models.Playlist:
        """Downloads and parses playlist data for a given playlist ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            playlist_id: The ID of the playlist to get.

        Returns:
            A Playlist model containing the parsed data.
        """
        response = self.download(playlist_id)
        return self.parse(response)

    def extract_bucket_playlist(
        self,
        data: models.Playlist,
        *,
        update: bool = True,
    ) -> bucket_playlist_models.BucketPlaylist:
        """Extract the playlist bucket element from playlist data.

        Args:
            data: Playlist data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A PlaylistBucketPlaylist model containing the parsed data.
        """
        for element in data.elements:
            if element.field_type == "bucket" and element.attributes.type == "playlist":
                dumped_bucket_playlist = self._dump_response(element)
                return BucketPlaylist().parse(dumped_bucket_playlist, update=update)

        msg = "No bucket playlist element found in playlist data"
        raise ValueError(msg)


class BucketPlaylist(BaseExtractor[bucket_playlist_models.BucketPlaylist]):
    """Provides methods to manage the playlist bucket element from playlist data."""

    @cached_property
    @override
    def _response_model(self) -> type[bucket_playlist_models.BucketPlaylist]:
        """Return the Pydantic model class for this client."""
        return bucket_playlist_models.BucketPlaylist

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> bucket_playlist_models.BucketPlaylist:
        """Parses playlist bucket data into a PlaylistBucketPlaylist model.

        Args:
            data: The playlist bucket data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A PlaylistBucketPlaylist model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return bucket_playlist_models.BucketPlaylist.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the folder name for this extractor's models."""
        return "playlist/bucket/playlist"
