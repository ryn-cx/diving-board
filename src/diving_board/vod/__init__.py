"""Contains the Vod class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL
from diving_board.vod.bucket import VodBucket
from diving_board.vod.hero import VodHero
from diving_board.vod.models import VodModel
from diving_board.vod.tabs import VodTabs
from diving_board.vod.text_block import VodTextBlock

if TYPE_CHECKING:
    from diving_board.vod.bucket.models import VodBucketModel
    from diving_board.vod.hero.models import VodHeroModel
    from diving_board.vod.tabs.models import VodTabsModel
    from diving_board.vod.text_block.models import VodTextBlockModel


class Vod(BaseEndpoint[VodModel]):
    """Manage the vod file."""

    _response_model = VodModel

    def download(
        self,
        vod_id: int | str,
        timezone: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the vod file.

        Raises:
            HTTPError: If vod_id is invalid.

        Example request: https://www.hidive.com/video/655773?showInterstitial=true
            GET /api/v1/view?type=vod&id=655773&timezone=America%2FLos_Angeles HTTP/2
            Host: dce-frontoffice.imggaming.com
            User-Agent: __REDACTED__
            Accept: application/json, text/plain, */*
            Accept-Language: en-US
            Accept-Encoding: gzip, deflate, br, zstd
            Referer: https://www.hidive.com/
            Content-Type: application/json
            x-api-key: 857a1e5d-e35e-4fdf-805b-a87b6f8364bf
            app: dice
            Realm: dce.hidive
            x-app-var: 6.60.0.5aaf921
            Authorization: Bearer __REDACTED__
            Origin: https://www.hidive.com
            Connection: keep-alive
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: cross-site
        """
        return self._client.download(
            f"{BASE_API_URL}/api/v1/view",
            {
                "type": "vod",
                "id": int(vod_id),
                "timezone": timezone or self._client.timezone,
            },
            log_id=f"{self.__class__.__name__} {vod_id}",
        )

    def get(self, vod_id: int | str, timezone: str | None = None) -> VodModel:
        """Downloads and parses the vod file.

        Raises:
            HTTPError: If vod_id is invalid.
        """
        data = self.download(vod_id, timezone)
        return self.parse(data)

    def extract_hero(
        self,
        data: VodModel,
        *,
        update_model: bool = True,
    ) -> VodHeroModel:
        """Extract the hero element from Vod."""
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
        """Extract the tabs element from Vod."""
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
        """Extract the bucket element from Vod."""
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
        """Extract the text block element from Vod."""
        return self._extract_element(
            data.elements,
            "textBlock",
            VodTextBlock,
            update_model=update_model,
        )
