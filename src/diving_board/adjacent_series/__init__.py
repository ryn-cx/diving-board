# TODO: Validate
"""Contains the AdjacentSeries class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from diving_board.adjacent_series.models import (
    AdjacentSeriesModel,
    model_validate_json,
)
from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL
from diving_board.exceptions import AdjacentSeriesNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class AdjacentSeries(BaseEndpoint):
    """Manage the adjacent series file, the seasons either side of one season.

    Source: https://www.hidive.com/season/{season_id}

    Example request:
        - GET /api/v4/series/{series_id}/adjacentTo/{season_id}?
            - size=25
            - HTTP/2
        - Host: dce-frontoffice.imggaming.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/plain, */*
        - Referer: https://www.hidive.com/
        - Content-Type: application/json
        - x-api-key: __REDACTED__
        - app: dice
        - Realm: dce.hidive
        - Authorization: Bearer __REDACTED__
        - Origin: https://www.hidive.com
    """

    # TODO: Validate
    def __call__(
        self,
        series_id: int | str,
        season_id: int | str,
        *,
        size: int = 25,
    ) -> AdjacentSeriesModel:
        """Look the adjacent seasons up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(series_id, season_id, size=size), log_id)

    # TODO: Validate
    def download(
        self,
        series_id: int | str,
        season_id: int | str,
        *,
        size: int = 25,
    ) -> str:
        """Download the adjacent series file."""
        log_id = self.get_log_id(self.download, locals())
        url = (
            f"{BASE_API_URL}/api/v4/series/{int(series_id)}/adjacentTo/{int(season_id)}"
        )
        try:
            return self._client.download(url, params={"size": size}, log_id=log_id)
        except ResourceNotFoundError as err:
            raise AdjacentSeriesNotFoundError(
                int(series_id),
                int(season_id),
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> AdjacentSeriesModel:
        """Read a downloaded adjacent series file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
