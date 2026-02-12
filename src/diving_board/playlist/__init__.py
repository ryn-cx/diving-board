"""Playlist API endpoint."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any, override

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.playlist.bucket import PlaylistBucket
from diving_board.playlist.hero import PlaylistHero
from diving_board.playlist.models import PlaylistModel
from diving_board.playlist.tabs import PlaylistTabs
from diving_board.playlist.text_block import PlaylistTextBlock

if TYPE_CHECKING:
    from diving_board.playlist.bucket.model import PlaylistBucketModel
    from diving_board.playlist.hero.model import PlaylistHeroModel
    from diving_board.playlist.tabs.model import PlaylistTabsModel
    from diving_board.playlist.text_block.model import PlaylistTextBlockModel


class Playlist(BaseEndpoint[PlaylistModel]):
    """Provides methods to download, parse, and retrieve playlist data."""

    @cached_property
    @override
    def _response_model(self) -> type[PlaylistModel]:
        return PlaylistModel

    def download(self, playlist_id: int, timezone: str = "") -> dict[str, Any]:
        """Downloads playlist data for a given playlist.

        Args:
            playlist_id: The ID of the playlist to download.
            timezone: The timezone to use for the request.

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
        params = {
            "type": "playlist",
            "id": playlist_id,
            "timezone": timezone or self._client.timezone,
        }
        return self._client.download_api_request(endpoint, params)

    def get(self, playlist_id: int, timezone: str = "") -> PlaylistModel:
        """Downloads and parses playlist data for a given playlist.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            playlist_id: The ID of the playlist to get.
            timezone: The timezone to use for the request.

        Returns:
            A Playlist model containing the parsed data.
        """
        response = self.download(playlist_id, timezone)
        return self.parse(response)

    def extract_hero(
        self,
        data: PlaylistModel,
        *,
        update: bool = True,
    ) -> PlaylistHeroModel:
        """Extract the hero element from playlist data.

        Args:
            data: Playlist data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A PlaylistHeroModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "hero",
            PlaylistHero,
            update=update,
        )

    def extract_tabs(
        self,
        data: PlaylistModel,
        *,
        update: bool = True,
    ) -> PlaylistTabsModel:
        """Extract the tabs element from playlist data.

        Args:
            data: Playlist data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A PlaylistTabsModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "tabs",
            PlaylistTabs,
            update=update,
        )

    def extract_bucket(
        self,
        data: PlaylistModel,
        bucket_type: str,
        *,
        update: bool = True,
    ) -> PlaylistBucketModel:
        """Extract a bucket element from playlist data.

        Args:
            data: Playlist data to extract from.
            bucket_type: The bucket subtype to extract (e.g. "playlist", "related").
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A PlaylistBucketModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "bucket",
            PlaylistBucket,
            attribute_type=bucket_type,
            update=update,
        )

    def extract_text_block(
        self,
        data: PlaylistModel,
        *,
        update: bool = True,
    ) -> PlaylistTextBlockModel:
        """Extract the text block element from playlist data.

        Args:
            data: Playlist data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A PlaylistTextBlockModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "textBlock",
            PlaylistTextBlock,
            update=update,
        )
