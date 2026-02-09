"""Season API endpoint."""

from __future__ import annotations

from functools import cached_property
from typing import Any, override

from diving_board.base_api_endpoint import BaseEndpoint, BaseExtractor
from diving_board.season import models
from diving_board.season.bucket.related import models as bucket_related_models
from diving_board.season.bucket.season import models as bucket_season_models
from diving_board.season.hero import models as hero_models
from diving_board.season.series import models as series_models


class Season(BaseEndpoint[models.Season]):
    """Provides methods to download, parse, and retrieve season data.

    Interacts with the season API endpoint.
    """

    @cached_property
    @override
    def _response_model(self) -> type[models.Season]:
        """Return the Pydantic model class for this client."""
        return models.Season

    def download(self, season_id: int) -> dict[str, Any]:
        """Downloads season data for a given season ID.

        Args:
            season_id: The ID of the season to download.

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
        params: dict[str, str | int] = {
            "type": "season",
            "id": season_id,
            "timezone": self._client.timezone,
        }
        return self._client.download_api_request(endpoint, params)

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> models.Season:
        """Parses season data into a Season model.

        Args:
            data: The season data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A Season model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return models.Season.model_validate(data)

    def get(
        self,
        season_id: int,
    ) -> models.Season:
        """Downloads and parses season data for a given season ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            season_id: The ID of the season to get.

        Returns:
            A Season model containing the parsed data.
        """
        response = self.download(season_id)
        return self.parse(response)

    def extract_bucket_related(
        self,
        data: models.Season,
        *,
        update: bool = True,
    ) -> bucket_related_models.SeasonBucketRelated:
        """Extract the related bucket element from season data.

        Args:
            data: Season data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonBucketRelated model containing the parsed data.
        """
        for element in data.elements:
            if element.field_type == "bucket" and element.attributes.type == "related":
                dumped_bucket_related = self._dump_response(element)
                return BucketRelated().parse(dumped_bucket_related, update=update)

        msg = "No related bucket element found in season data"
        raise ValueError(msg)

    def extract_bucket_season(
        self,
        data: models.Season,
        *,
        update: bool = True,
    ) -> bucket_season_models.SeasonBucketSeason:
        """Extract the season bucket element from season data.

        Args:
            data: Season data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonBucketSeason model containing the parsed data.
        """
        for element in data.elements:
            if element.field_type == "bucket" and element.attributes.type == "season":
                dumped_bucket_season = self._dump_response(element)
                return BucketSeason().parse(dumped_bucket_season, update=update)

        msg = "No bucket season element found in season data"
        raise ValueError(msg)

    def extract_series(
        self,
        data: models.Season,
        *,
        update: bool = True,
    ) -> series_models.SeasonSeries:
        """Extract the series element from season data.

        Args:
            data: Season data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonSeries model containing the parsed data.
        """
        for element in data.elements:
            if element.field_type == "series":
                dumped_series = self._dump_response(element)
                return Series().parse(dumped_series, update=update)

        msg = "No series element found in season data"
        raise ValueError(msg)

    def extract_hero(
        self,
        data: models.Season,
        *,
        update: bool = True,
    ) -> hero_models.SeasonHero:
        """Extract the hero element from season data.

        Args:
            data: Season data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonHero model containing the parsed data.
        """
        for element in data.elements:
            if element.field_type == "hero":
                dumped_hero = self._dump_response(element)
                return Hero().parse(dumped_hero, update=update)

        msg = "No hero element found in season data"
        raise ValueError(msg)


class BucketRelated(BaseExtractor[bucket_related_models.SeasonBucketRelated]):
    """Provides methods to manage the related bucket element from season data."""

    @cached_property
    @override
    def _response_model(self) -> type[bucket_related_models.SeasonBucketRelated]:
        """Return the Pydantic model class for this client."""
        return bucket_related_models.SeasonBucketRelated

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> bucket_related_models.SeasonBucketRelated:
        """Parses related bucket data into a SeasonBucketRelated model.

        Args:
            data: The related bucket data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonBucketRelated model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return bucket_related_models.SeasonBucketRelated.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the folder name for this extractor's models."""
        return "season/bucket/related"


class BucketSeason(BaseExtractor[bucket_season_models.SeasonBucketSeason]):
    """Provides methods to manage the season bucket element from season data."""

    @cached_property
    @override
    def _response_model(self) -> type[bucket_season_models.SeasonBucketSeason]:
        """Return the Pydantic model class for this client."""
        return bucket_season_models.SeasonBucketSeason

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> bucket_season_models.SeasonBucketSeason:
        """Parses season bucket data into a SeasonBucketSeason model.

        Args:
            data: The season bucket data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonBucketSeason model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return bucket_season_models.SeasonBucketSeason.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the folder name for this extractor's models."""
        return "season/bucket/season"


class Series(BaseExtractor[series_models.SeasonSeries]):
    """Provides methods to manage the series element from season data."""

    @cached_property
    @override
    def _response_model(self) -> type[series_models.SeasonSeries]:
        """Return the Pydantic model class for this client."""
        return series_models.SeasonSeries

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> series_models.SeasonSeries:
        """Parses series data into a SeasonSeries model.

        Args:
            data: The series data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonSeries model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return series_models.SeasonSeries.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the folder name for this extractor's models."""
        return "season/series"


class Hero(BaseExtractor[hero_models.SeasonHero]):
    """Provides methods to manage the hero element from season data."""

    @cached_property
    @override
    def _response_model(self) -> type[hero_models.SeasonHero]:
        """Return the Pydantic model class for this client."""
        return hero_models.SeasonHero

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> hero_models.SeasonHero:
        """Parses hero data into a SeasonHero model.

        Args:
            data: The hero data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A SeasonHero model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return hero_models.SeasonHero.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the folder name for this extractor's models."""
        return "season/hero"
