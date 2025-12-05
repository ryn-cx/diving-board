from typing import Any, Literal

from diving_board.protocol import DivingBoardProtocol
from diving_board.season import models
from diving_board.season.bucket import models as bucket_models
from diving_board.season.series import models as series_models


class SeasonMixin(DivingBoardProtocol):
    def download_season(
        self,
        season_id: int,
        *,
        timezone: str = "America/Los_Angeles",
    ) -> dict[str, Any]:
        return self._get_api_request(
            "api/v1/view",
            {"type": "season", "id": season_id, "timezone": timezone},
        )

    def parse_season(
        self,
        data: dict[str, Any],
        *,
        update: bool = False,
    ) -> models.Season:
        if update:
            return self.parse_response(models.Season, data, "season")

        return models.Season.model_validate(data)

    def get_season(
        self,
        season_id: int,
        *,
        timezone: str = "America/Los_Angeles",
    ) -> models.Season:
        data = self.download_season(season_id, timezone=timezone)
        return self.parse_season(data, update=True)

    def extract_season_bucket(
        self,
        data: models.Season,
        subtype: Literal["related", "season"] = "season",
        *,
        update: bool = False,
    ) -> bucket_models.SeasonBucketSeason:
        for element in data.elements:
            if element.field_type == "bucket" and element.attributes.type == subtype:
                season_data = element.attributes.model_dump()

                if update:
                    return self.parse_response(
                        bucket_models.SeasonBucketSeason,
                        season_data,
                        "season/bucket",
                    )

                return bucket_models.SeasonBucketSeason.model_validate(season_data)

        msg = "No bucket season element found in season data"
        raise ValueError(msg)

    def extract_season_series(
        self,
        data: models.Season,
        *,
        update: bool = False,
    ) -> series_models.SeasonSeries:
        for element in data.elements:
            if element.field_type == "series":
                season_data = element.model_dump()

                if update:
                    return self.parse_response(
                        series_models.SeasonSeries,
                        season_data,
                        "season/series",
                    )

                return series_models.SeasonSeries.model_validate(season_data)

        msg = "No bucket season element found in season data"
        raise ValueError(msg)
