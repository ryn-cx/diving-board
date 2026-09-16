# TODO: Validate
"""Contains the ContentGrid class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL
from diving_board.content_grid.models import ContentGridModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

SERIES_GRID_VIEW_CONFIG_ID = "266043db-02a8-4646-82bc-9da24127ccdc"
"""The grid holding every series."""

MOVIES_GRID_VIEW_CONFIG_ID = "05d9e1ad-8dca-4dd9-8aac-5c1b5c660115"
"""The grid holding every movie."""

RESULTS_PER_PAGE = 48
SORT = "publicationDate"
SORT_DIRECTION = "DESC"


# TODO: Validate
class ContentGrid(BaseEndpoint):
    """Manage the content grid file, one page of cards at a time.

    Source: https://www.hidive.com/library

    Example request:
        - GET /api/v1/view/content-grid?
            - sort=publicationDate&
            - sortDirection=DESC&
            - lastSeen={last_seen}&
            - gridViewConfigId={grid_view_config_id}&
            - rpp=48&
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
    def __call__(  # noqa: PLR0913
        self,
        grid_view_config_id: str = SERIES_GRID_VIEW_CONFIG_ID,
        *,
        last_seen: str | None = None,
        timezone: str | None = None,
        results_per_page: int = RESULTS_PER_PAGE,
        sort: str = SORT,
        sort_direction: str = SORT_DIRECTION,
    ) -> ContentGridModel:
        """Look one page of a content grid up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                grid_view_config_id,
                last_seen=last_seen,
                timezone=timezone,
                results_per_page=results_per_page,
                sort=sort,
                sort_direction=sort_direction,
            ),
            log_id,
        )

    # TODO: Validate
    def download(  # noqa: PLR0913
        self,
        grid_view_config_id: str = SERIES_GRID_VIEW_CONFIG_ID,
        *,
        last_seen: str | None = None,
        timezone: str | None = None,
        results_per_page: int = RESULTS_PER_PAGE,
        sort: str = SORT,
        sort_direction: str = SORT_DIRECTION,
    ) -> str:
        """Download one page of a content grid file.

        Args:
            grid_view_config_id: Which grid to read. The website has one for
                series and one for movies.
            last_seen: The token the page before this one handed back. Left out
                the API answers with the first page.
            timezone: The timezone the dates are written in.
            results_per_page: How many cards one page carries.
            sort: The field the cards are ordered by.
            sort_direction: `ASC` or `DESC`.
        """
        log_id = self.get_log_id(self.download, locals())
        params: dict[str, Any] = {
            "sort": sort,
            "sortDirection": sort_direction,
            "gridViewConfigId": grid_view_config_id,
            "rpp": results_per_page,
            "timezone": timezone or self._client.timezone,
        }

        if last_seen:
            params["lastSeen"] = last_seen

        return self._client.download(
            f"{BASE_API_URL}/api/v1/view/content-grid",
            params=params,
            log_id=log_id,
        )

    # TODO: Validate
    def download_all(
        self,
        grid_view_config_id: str = SERIES_GRID_VIEW_CONFIG_ID,
        *,
        timezone: str | None = None,
        results_per_page: int = RESULTS_PER_PAGE,
        sort: str = SORT,
        sort_direction: str = SORT_DIRECTION,
    ) -> list[str]:
        """Download every page of a content grid."""
        pages: list[str] = []
        last_seen: str | None = None

        while True:
            page = self.download(
                grid_view_config_id,
                last_seen=last_seen,
                timezone=timezone,
                results_per_page=results_per_page,
                sort=sort,
                sort_direction=sort_direction,
            )
            pages.append(page)
            last_seen = self.next_page_token(page)
            if not last_seen:
                return pages

    # TODO: Validate
    @staticmethod
    def next_page_token(response: str) -> str | None:
        """Return what the next page is asked for, or None on the last page."""
        elements = json.loads(response)["elements"]
        card_list = next(
            element["attributes"]
            for element in elements
            if element["$type"] == "cardList"
        )
        # The last page has nothing to go to next, so it carries no actions at
        # all rather than an empty one.
        actions = card_list.get("actions")
        if not actions:
            return None
        token: str = actions["next"]["action"]["data"]["currentSearch"]["lastSeen"]
        return token

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ContentGridModel:
        """Load a content grid file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    def load_pages(self, pages: list[str]) -> list[ContentGridModel]:
        """Read the pages `download_all` returns into their models."""
        return [self.load(page) for page in pages]
