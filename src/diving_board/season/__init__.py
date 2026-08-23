# TODO: Validate
"""Contains the Season class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL
from diving_board.exceptions import ResourceNotFoundError, SeasonNotFoundError
from diving_board.season.models import SeasonModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Season(BaseEndpoint):
    """Manage the season file, which lists the episodes the season is made of.

    Source: https://www.hidive.com/season/{season_id}

    Example request:
        - GET /api/v1/view?
            - type=season&
            - id={season_id}&
            - timezone=America%2FLos_Angeles
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
        season_id: int | str,
        *,
        timezone: str | None = None,
    ) -> SeasonModel:
        """Look the season up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(season_id, timezone=timezone),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        season_id: int | str,
        *,
        timezone: str | None = None,
    ) -> str:
        """Download the season file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"{BASE_API_URL}/api/v1/view",
                params={
                    "type": "season",
                    "id": int(season_id),
                    "timezone": timezone or self._client.timezone,
                },
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeasonNotFoundError(
                int(season_id),
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, int(season_id))

    # TODO: Validate
    def _validate_download(self, response: str, season_id: int) -> str:
        """Check that the file is for the season that was asked for."""
        metadata = json.loads(response)["metadata"]
        if metadata["currentSeason"]["seasonId"] != season_id:
            raise SeasonNotFoundError(season_id, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SeasonModel:
        """Read a downloaded season file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
