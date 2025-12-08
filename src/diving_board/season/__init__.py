from typing import Any

from pydantic import BaseModel

from diving_board.protocol import DivingBoardProtocol
from diving_board.season import models
from diving_board.season.bucket.related import models as season_bucket_related_models
from diving_board.season.bucket.season import models as season_bucket_season_models
from diving_board.season.series import models as series_models


class SeasonMixin(DivingBoardProtocol):
    def download_season(self, season_id: int) -> dict[str, Any]:
        # The URL used for the api call can be found on the season page for the series:
        # https://www.hidive.com/season/33099
        # Example API URL:
        # https://dce-frontoffice.imggaming.com/api/v1/view?type=season&id=18874&timezone=America%2FLos_Angeles

        endpoint = "api/v1/view"
        parms: dict[str, str | int] = {
            "type": "season",
            "id": season_id,
            "timezone": self.timezone,
        }
        return self._download_api_request(endpoint, parms)

    def parse_season(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> models.Season:
        if update:
            return self.parse_response(models.Season, data, "season")

        return models.Season.model_validate(data)

    def get_season(
        self,
        season_id: int,
    ) -> models.Season:
        response = self.download_season(season_id)
        return self.parse_season(response)

    def extract_season_bucket_related(
        self,
        data: models.Season,
        *,
        update: bool = True,
    ) -> season_bucket_related_models.SeasonBucketRelated:
        return self._extract_season_generic(
            data,
            season_bucket_related_models.SeasonBucketRelated,
            "related",
            update=update,
        )

    def extract_season_bucket_season(
        self,
        data: models.Season,
        *,
        update: bool = True,
    ) -> season_bucket_season_models.SeasonBucketSeason:
        return self._extract_season_generic(
            data,
            season_bucket_season_models.SeasonBucketSeason,
            "season",
            update=update,
        )

    def _extract_season_generic[T: BaseModel](
        self,
        data: models.Season,
        response_model: type[T],
        attribute_type: str,
        *,
        update: bool = True,
    ) -> T:
        for element in data.elements:
            if (
                element.field_type == "bucket"
                and element.attributes.type == attribute_type
            ):
                season_data = element.attributes.model_dump(mode="json")

                if update:
                    return self.parse_response(
                        response_model,
                        season_data,
                        f"season/bucket/{attribute_type}",
                    )

                return response_model.model_validate(season_data)

        msg = "No bucket season element found in season data"
        raise ValueError(msg)

    def extract_season_series(
        self,
        data: models.Season,
        *,
        update: bool = True,
    ) -> series_models.SeasonSeries:
        for element in data.elements:
            if element.field_type == "series":
                season_data = element.model_dump(mode="json")

                if update:
                    return self.parse_response(
                        series_models.SeasonSeries,
                        season_data,
                        "season/series",
                    )

                return series_models.SeasonSeries.model_validate(season_data)

        msg = "No bucket season element found in season data"
        raise ValueError(msg)
