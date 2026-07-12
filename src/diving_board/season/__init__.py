"""Contains the Season class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL
from diving_board.season.bucket.related import SeasonBucketRelated
from diving_board.season.bucket.season import SeasonBucketSeason
from diving_board.season.hero import SeasonHero
from diving_board.season.models import SeasonModel
from diving_board.season.series import SeasonSeries
from diving_board.season.tabs import SeasonTabs
from diving_board.season.text_block import SeasonTextBlock

if TYPE_CHECKING:
    from diving_board.season.bucket.related.model import SeasonBucketRelatedModel
    from diving_board.season.bucket.season.model import SeasonBucketSeasonModel
    from diving_board.season.hero.model import SeasonHeroModel
    from diving_board.season.series.model import SeasonSeriesModel
    from diving_board.season.tabs.model import SeasonTabsModel
    from diving_board.season.text_block.model import SeasonTextBlockModel


class Season(BaseEndpoint[SeasonModel]):
    """Manage the season file."""

    _response_model = SeasonModel

    def download(self, season_id: int, timezone: str | None = None) -> dict[str, Any]:
        """Downloads the season file.

        Raises:
            HTTPError: If season_id is invalid.

        Example request: https://www.hidive.com/season/24579?seriesId=2311
            GET /api/v1/view?type=season&id=24579&timezone=America%2FLos_Angeles HTTP/2
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
            Connection: keep-alive
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: cross-site
            Priority: u=4
            TE: trailers
        """
        return self._client.download(
            f"{BASE_API_URL}/api/v1/view",
            {
                "type": "season",
                "id": season_id,
                "timezone": timezone or self._client.timezone,
            },
            f"season {season_id}",
        )

    def get(
        self,
        season_id: int,
        timezone: str | None = None,
    ) -> SeasonModel:
        """Downloads and parses the season file.

        Raises:
            HTTPError: If season_id is invalid.
        """
        response = self.download(season_id, timezone)
        return self.parse(response)

    def extract_hero(
        self,
        data: SeasonModel,
        *,
        update_model: bool = True,
    ) -> SeasonHeroModel:
        """Extract the hero element from Season."""
        return self._extract_element(
            data.elements,
            "hero",
            SeasonHero,
            update_model=update_model,
        )

    def extract_tabs(
        self,
        data: SeasonModel,
        *,
        update_model: bool = True,
    ) -> SeasonTabsModel:
        """Extract the tabs element from Season."""
        return self._extract_element(
            data.elements,
            "tabs",
            SeasonTabs,
            update_model=update_model,
        )

    def extract_series(
        self,
        data: SeasonModel,
        *,
        update_model: bool = True,
    ) -> SeasonSeriesModel:
        """Extract the series element from Season."""
        return self._extract_element(
            data.elements,
            "series",
            SeasonSeries,
            update_model=update_model,
        )

    def extract_bucket_season(
        self,
        data: SeasonModel,
        *,
        update_model: bool = True,
    ) -> SeasonBucketSeasonModel:
        """Extract the season-type bucket element from Season."""
        return self._extract_typed_element(
            data.elements,
            "bucket",
            "season",
            SeasonBucketSeason,
            update_model=update_model,
        )

    def extract_bucket_related(
        self,
        data: SeasonModel,
        *,
        update_model: bool = True,
    ) -> SeasonBucketRelatedModel:
        """Extract the related-type bucket element from Season."""
        return self._extract_typed_element(
            data.elements,
            "bucket",
            "related",
            SeasonBucketRelated,
            update_model=update_model,
        )

    def extract_text_block(
        self,
        data: SeasonModel,
        *,
        update_model: bool = True,
    ) -> SeasonTextBlockModel:
        """Extract the text block element from Season."""
        return self._extract_element(
            data.elements,
            "textBlock",
            SeasonTextBlock,
            update_model=update_model,
        )
