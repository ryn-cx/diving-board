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
        size: int = 25,
    ) -> dict[str, Any]:
        # The URL used for the api call can be found on the season page for the series:
        # https://www.hidive.com/season/33099
        # Example API URL:
        # https://dce-frontoffice.imggaming.com/api/v4/series/3592/adjacentTo/33099?size=25

        endpoint = f"api/v4/series/{series_id}/adjacentTo/{season_id}"
        params = {"size": size}
        return self._download_api_request(endpoint, params)

    def parse_adjacent_series(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> models.AdjacentSeries:
        if update:
            return self.parse_response(models.AdjacentSeries, data, "adjacent_series")

        return models.AdjacentSeries.model_validate(data)

    def get_adjacent_series(
        self,
        series_id: int,
        season_id: int,
        size: int = 25,
    ) -> models.AdjacentSeries:
        response = self.download_adjacent_series(
            series_id=series_id,
            season_id=season_id,
            size=size,
        )
        return self.parse_adjacent_series(response)
