from typing import Any

from diving_board.protocol import DivingBoardProtocol
from diving_board.season import models
from diving_board.season.bucket.season import models as bucket_season_models


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

    def extract_season_bucket_season(
        self,
        data: models.Season,
        *,
        update: bool = False,
    ) -> bucket_season_models.SeasonBucketSeason:
        for element in data.elements:
            if element.field_type == "bucket" and element.attributes.type == "season":
                season_data = element.attributes.model_dump()

                if update:
                    return self.parse_response(
                        bucket_season_models.SeasonBucketSeason,
                        season_data,
                        "season/bucket/season",
                    )

                return bucket_season_models.SeasonBucketSeason.model_validate(
                    season_data,
                )

        msg = "No bucket season element found in season data"
        raise ValueError(msg)
