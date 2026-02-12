"""Season API endpoint."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any, override

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.season.bucket import SeasonBucket
from diving_board.season.hero import SeasonHero
from diving_board.season.models import SeasonModel
from diving_board.season.series import SeasonSeries
from diving_board.season.tabs import SeasonTabs
from diving_board.season.text_block import SeasonTextBlock

if TYPE_CHECKING:
    from diving_board.season.bucket.model import SeasonBucketModel
    from diving_board.season.hero.model import SeasonHeroModel
    from diving_board.season.series.model import SeasonSeriesModel
    from diving_board.season.tabs.model import SeasonTabsModel
    from diving_board.season.text_block.model import SeasonTextBlockModel


class Season(BaseEndpoint[SeasonModel]):
    """Provides methods to download, parse, and retrieve season data."""

    @cached_property
    @override
    def _response_model(self) -> type[SeasonModel]:
        return SeasonModel

    def download(self, season_id: int, timezone: str = "") -> dict[str, Any]:
        """Downloads season data for a given season ID.

        Args:
            season_id: The ID of the season to download.
            timezone: The timezone to use for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        # Example request headers from https://www.hidive.com/season/19078
        """GET /api/v1/view?type=season&id=19078&timezone=America%2FLos_Angeles HTTP/2
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
        params = {
            "type": "season",
            "id": season_id,
            "timezone": timezone or self._client.timezone,
        }
        return self._client.download_api_request(endpoint, params)

    def get(
        self,
        season_id: int,
        timezone: str = "",
    ) -> SeasonModel:
        """Downloads and parses season data for a given season ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            season_id: The ID of the season to get.
            timezone: The timezone to use for the request.

        Returns:
            A Season model containing the parsed data.
        """
        response = self.download(season_id, timezone)
        return self.parse(response)

    def extract_hero(
        self,
        data: SeasonModel,
        *,
        update: bool = True,
    ) -> SeasonHeroModel:
        """Extract the hero element from season data.

        Args:
            data: Season data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonHeroModel model containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "hero",
            SeasonHero,
            update=update,
        )

    def extract_tabs(
        self,
        data: SeasonModel,
        *,
        update: bool = True,
    ) -> SeasonTabsModel:
        """Extract the tabs element from season data.

        Args:
            data: Season data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonTabsModel model containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "tabs",
            SeasonTabs,
            update=update,
        )

    def extract_series(
        self,
        data: SeasonModel,
        *,
        update: bool = True,
    ) -> SeasonSeriesModel:
        """Extract the series element from season data.

        Args:
            data: Season data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonSeriesModel model containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "series",
            SeasonSeries,
            update=update,
        )

    def extract_bucket(
        self,
        data: SeasonModel,
        bucket_type: str,
        *,
        update: bool = True,
    ) -> SeasonBucketModel:
        """Extract a bucket element from season data.

        Args:
            data: Season data to extract from.
            bucket_type: The bucket subtype to extract (e.g. "season", "related").
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonBucketModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "bucket",
            SeasonBucket,
            attribute_type=bucket_type,
            update=update,
        )

    def extract_text_block(
        self,
        data: SeasonModel,
        *,
        update: bool = True,
    ) -> SeasonTextBlockModel:
        """Extract the text block element from season data.

        Args:
            data: Season data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonTextBlockModel model containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "textBlock",
            SeasonTextBlock,
            update=update,
        )
