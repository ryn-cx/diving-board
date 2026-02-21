"""VOD API endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.vod.bucket import VodBucket
from diving_board.vod.hero import VodHero
from diving_board.vod.models import VodModel
from diving_board.vod.tabs import VodTabs
from diving_board.vod.text_block import VodTextBlock

if TYPE_CHECKING:
    from diving_board.vod.bucket.model import VodBucketModel
    from diving_board.vod.hero.model import VodHeroModel
    from diving_board.vod.tabs.model import VodTabsModel
    from diving_board.vod.text_block.model import VodTextBlockModel


class Vod(BaseEndpoint[VodModel]):
    """Provides methods to download, parse, and retrieve VOD data."""

    _response_model = VodModel

    def download(self, vod_id: int, timezone: str = "") -> dict[str, Any]:
        """Downloads VOD data for a given VOD ID.

        Args:
            vod_id: The ID of the VOD to download.
            timezone: The timezone to use for the request.

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
            "timezone": timezone or self._client.timezone,
        }
        return self._client.download(endpoint, params)

    def get(self, vod_id: int, timezone: str = "") -> VodModel:
        """Downloads and parses VOD data for a given VOD ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            vod_id: The ID of the VOD to get.
            timezone: The timezone to use for the request.

        Returns:
            A Vod model containing the parsed data.
        """
        data = self.download(vod_id, timezone)
        return self.parse(data)

    def extract_hero(
        self,
        data: VodModel,
        *,
        update_model: bool = True,
    ) -> VodHeroModel:
        """Extract the hero element from VOD data.

        Args:
            data: VOD data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodHeroModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "hero",
            VodHero,
            update_model=update_model,
        )

    def extract_tabs(
        self,
        data: VodModel,
        *,
        update_model: bool = True,
    ) -> VodTabsModel:
        """Extract the tabs element from VOD data.

        Args:
            data: VOD data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodTabsModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "tabs",
            VodTabs,
            update_model=update_model,
        )

    def extract_bucket(
        self,
        data: VodModel,
        *,
        update_model: bool = True,
    ) -> VodBucketModel:
        """Extract the bucket element from VOD data.

        Args:
            data: VOD data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodBucketModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "bucket",
            VodBucket,
            update_model=update_model,
        )

    def extract_text_block(
        self,
        data: VodModel,
        *,
        update_model: bool = True,
    ) -> VodTextBlockModel:
        """Extract the text block element from VOD data.

        Args:
            data: VOD data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A VodTextBlockModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "textBlock",
            VodTextBlock,
            update_model=update_model,
        )
