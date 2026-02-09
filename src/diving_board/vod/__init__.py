"""VOD API endpoint."""

from __future__ import annotations

from datetime import datetime
from functools import cached_property
from typing import Any, override

from diving_board.base_api_endpoint import BaseEndpoint, BaseExtractor
from diving_board.vod import models
from diving_board.vod.bucket import models as bucket_models
from diving_board.vod.hero import models as hero_models
from diving_board.vod.tabs import models as tabs_models
from diving_board.vod.text_block import models as text_block_models


class Vod(BaseEndpoint[models.Vod]):
    """Provides methods to download, parse, and retrieve VOD data."""

    @cached_property
    @override
    def _response_model(self) -> type[models.Vod]:
        """Return the Pydantic model class for this client."""
        return models.Vod

    def download(self, vod_id: int) -> dict[str, Any]:
        """Downloads VOD data for a given VOD ID.

        Args:
            vod_id: The ID of the VOD to download.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        # Example request headers from https://www.hidive.com/interstitial/542391
        """GET /api/v1/view?type=vod&id=542391&timezone=America%2FLos_Angeles HTTP/2
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
            Priority: u=4
            TE: trailers"""
        endpoint = "api/v1/view"
        params: dict[str, str | int] = {
            "type": "vod",
            "id": vod_id,
            "timezone": self._client.timezone,
        }
        return self._client.download_api_request(endpoint, params)

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> models.Vod:
        """Parses VOD data into a Vod model.

        Args:
            data: The VOD data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A Vod model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return models.Vod.model_validate(data)

    def get(self, vod_id: int) -> models.Vod:
        """Downloads and parses VOD data for a given VOD ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            vod_id: The ID of the VOD to get.

        Returns:
            A Vod model containing the parsed data.
        """
        data = self.download(vod_id)
        return self.parse(data)

    def extract_original_premiere(
        self,
        data: models.Vod,
    ) -> datetime:
        """Extract the Original Premiere date from a VOD.

        Args:
            data: VOD data

        Returns:
            Original premiere date string or None if not found
        """
        for element in data.elements:
            if element.field_type == "hero":
                for content_item in element.attributes.content or []:
                    if content_item.field_type == "tagList":
                        # Search through tags for "Original Premiere: ..."
                        for tag in content_item.attributes.tags or []:
                            if (
                                tag.field_type == "textblock"
                                and tag.attributes.text
                                and tag.attributes.text.startswith("Original Premiere:")
                            ):
                                # Extract the date portion after "Original Premiere: "
                                date_string = tag.attributes.text
                                date = date_string.replace("Original Premiere: ", "")
                                return datetime.strptime(date, "%B %d, %Y").astimezone()

        msg = "Original Premiere date not found in VOD data"
        raise ValueError(msg)

    def extract_hero(
        self,
        data: models.Vod,
        *,
        update: bool = True,
    ) -> hero_models.VodHero:
        """Extract the hero element from VOD data.

        Args:
            data: VOD data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodHero model containing the parsed hero data.
        """
        for element in data.elements:
            if element.field_type == "hero":
                dumped_hero = self._dump_response(element)
                return Hero().parse(dumped_hero, update=update)

        msg = "No hero element found in VOD data"
        raise ValueError(msg)

    def extract_bucket(
        self,
        data: models.Vod,
        *,
        update: bool = True,
    ) -> bucket_models.VodBucket:
        """Extract the bucket element from VOD data.

        Args:
            data: VOD data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodBucket model containing the parsed bucket data.
        """
        for element in data.elements:
            if element.field_type == "bucket":
                dumped_bucket = self._dump_response(element)
                return Bucket().parse(dumped_bucket, update=update)

        msg = "No bucket element found in VOD data"
        raise ValueError(msg)

    def extract_tabs(
        self,
        data: models.Vod,
        *,
        update: bool = True,
    ) -> tabs_models.VodTabs:
        """Extract the tabs element from VOD data.

        Args:
            data: VOD data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodTabs model containing the parsed tabs data.
        """
        for element in data.elements:
            if element.field_type == "tabs":
                dumped_tabs = self._dump_response(element)
                return Tabs().parse(dumped_tabs, update=update)

        msg = "No tabs element found in VOD data"
        raise ValueError(msg)

    def extract_text_block(
        self,
        data: models.Vod,
        *,
        update: bool = True,
    ) -> text_block_models.VodTextBlock:
        """Extract the text block element from VOD data.

        Args:
            data: VOD data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodTextBlock model containing the parsed text block data.
        """
        for element in data.elements:
            if element.field_type == "textBlock":
                dumped_text_block = self._dump_response(element)
                return _TextBlock().parse(dumped_text_block, update=update)

        msg = "No textBlock element found in VOD data"
        raise ValueError(msg)


class Hero(BaseExtractor[hero_models.VodHero]):
    """Provides methods to manage the hero element from VOD data."""

    @cached_property
    @override
    def _response_model(self) -> type[hero_models.VodHero]:
        """Return the Pydantic model class for this client."""
        return hero_models.VodHero

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> hero_models.VodHero:
        """Parses hero data into a VodHero model.

        Args:
            data: The hero data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodHero model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return hero_models.VodHero.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the folder name for this extractor's models."""
        return "vod/hero"


class Bucket(BaseExtractor[bucket_models.VodBucket]):
    """Provides methods to manage the bucket element from VOD data."""

    @cached_property
    @override
    def _response_model(self) -> type[bucket_models.VodBucket]:
        """Return the Pydantic model class for this client."""
        return bucket_models.VodBucket

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> bucket_models.VodBucket:
        """Parses bucket data into a VodBucket model.

        Args:
            data: The bucket data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodBucket model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return bucket_models.VodBucket.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the folder name for this extractor's models."""
        return "vod/bucket"


class Tabs(BaseExtractor[tabs_models.VodTabs]):
    """Provides methods to manage the tabs element from VOD data."""

    @cached_property
    @override
    def _response_model(self) -> type[tabs_models.VodTabs]:
        """Return the Pydantic model class for this client."""
        return tabs_models.VodTabs

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> tabs_models.VodTabs:
        """Parses tabs data into a VodTabs model.

        Args:
            data: The tabs data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodTabs model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return tabs_models.VodTabs.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the folder name for this extractor's models."""
        return "vod/tabs"


class _TextBlock(BaseExtractor[text_block_models.VodTextBlock]):
    """Provides methods to manage the text block element from VOD data."""

    @cached_property
    @override
    def _response_model(self) -> type[text_block_models.VodTextBlock]:
        """Return the Pydantic model class for this client."""
        return text_block_models.VodTextBlock

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> text_block_models.VodTextBlock:
        """Parses text block data into a VodTextBlock model.

        Args:
            data: The text block data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodTextBlock model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return text_block_models.VodTextBlock.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the folder name for this extractor's models."""
        return "vod/text_block"
