from typing import Any

from diving_board.protocol import DivingBoardProtocol
from diving_board.season import models


class SeasonMixin(DivingBoardProtocol):
    def download_season(
        self,
        season_id: int,
        *,
        timezone: str = "America%2FLos_Angeles",
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
        timezone: str = "America%2FLos_Angeles",
    ) -> models.Season:
        data = self.download_season(season_id, timezone=timezone)
        return self.parse_season(data, update=True)
