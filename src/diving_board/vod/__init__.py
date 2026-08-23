# TODO: Validate
"""Contains the Vod class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL
from diving_board.exceptions import ResourceNotFoundError, VodNotFoundError
from diving_board.vod.models import VodModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Vod(BaseEndpoint):
    """Manage the video file, which is an episode or a film.

    Source: https://www.hidive.com/video/{vod_id}

    Example request:
        - GET /api/v1/view?
            - type=vod&
            - id={vod_id}&
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
        vod_id: int | str,
        *,
        timezone: str | None = None,
    ) -> VodModel:
        """Look the video up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(vod_id, timezone=timezone), log_id)

    # TODO: Validate
    def download(
        self,
        vod_id: int | str,
        *,
        timezone: str | None = None,
    ) -> str:
        """Download the video file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"{BASE_API_URL}/api/v1/view",
                params={
                    "type": "vod",
                    "id": int(vod_id),
                    "timezone": timezone or self._client.timezone,
                },
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise VodNotFoundError(int(vod_id), err.status_code, err.response) from err
        return self._validate_download(response, int(vod_id))

    # TODO: Validate
    def _validate_download(self, response: str, vod_id: int) -> str:
        """Check that the file is for the video that was asked for."""
        elements = json.loads(response)["elements"]
        tab_ids = [
            element["attributes"]["id"]
            for element in elements
            if element["$type"] == "tabs"
        ]
        if vod_id not in tab_ids:
            raise VodNotFoundError(vod_id, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> VodModel:
        """Read a downloaded video file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
