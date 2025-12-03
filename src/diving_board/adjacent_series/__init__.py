import logging
from typing import Any

from diving_board.adjacent_series import models
from diving_board.protocol import DivingBoardProtocol

logger = logging.getLogger(__name__)


class AdjecentSeariessMixin(DivingBoardProtocol):
    def download_adjacent_series(
        self,
        series_id: int,
        season_id: int,
    ) -> dict[str, Any]:
        return self._get_api_request(
            f"api/v4/series/{series_id}/adjacentTo/{season_id}",
            {"size": 25},
        )

    def parse_adjacent_series(
        self,
        data: dict[str, Any],
        *,
        update: bool = False,
    ) -> models.AdjacentSeries:
        if update:
            return self.parse_response(models.AdjacentSeries, data, "adjacent_series")

        return models.AdjacentSeries.model_validate(data)

    def get_adjacent_series(
        self,
        series_id: int,
        season_id: int,
    ) -> models.AdjacentSeries:
        data = self.download_adjacent_series(series_id, season_id)
        return self.parse_adjacent_series(data, update=True)
