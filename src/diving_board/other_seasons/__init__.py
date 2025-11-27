import logging
from typing import Any

from diving_board.protocol import DivingBoardProtocol

from .models import OtherSeasons

logger = logging.getLogger(__name__)


class OtherSeasonsMixin(DivingBoardProtocol):
    def download_other_seasons(
        self,
        series_id: int,
        season_id: int,
    ) -> dict[str, Any]:
        return self._get_api_request(
            f"api/v4/series/{series_id}/adjacentTo/{season_id}",
            {"size": 25},
        )

    def parse_other_seasons(
        self,
        data: dict[str, Any],
        *,
        update: bool = False,
    ) -> OtherSeasons:
        if update:
            return self.parse_response(OtherSeasons, data, "other_seasons")

        return OtherSeasons.model_validate(data)

    def get_other_seasons(self, series_id: int, season_id: int) -> OtherSeasons:
        data = self.download_other_seasons(series_id, season_id)
        return self.parse_other_seasons(data, update=True)
