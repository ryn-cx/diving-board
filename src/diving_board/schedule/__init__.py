# TODO: Validate
"""Contains the Schedule class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL
from diving_board.schedule.models import ScheduleModel, model_validate_json

if TYPE_CHECKING:
    from datetime import datetime

logger = getLogger(__name__)
logger.addHandler(NullHandler())

GROUPS_PER_PAGE = 7
ITEMS_PER_GROUP = 7


# TODO: Validate
class Schedule(BaseEndpoint):
    """Manage the release schedule file, one page at a time.

    Source: https://www.hidive.com/releases

    Example request:
        - GET /api/v1/view/schedule?
            - timezone=America%2FLos_Angeles&
            - groupsPerPage=7&
            - itemsPerGroup=7&
            - from=2026-06-01T00%3A00%3A00
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
        from_: datetime | None = None,
        *,
        last_seen: str | None = None,
        timezone: str | None = None,
        groups_per_page: int = GROUPS_PER_PAGE,
        items_per_group: int = ITEMS_PER_GROUP,
    ) -> ScheduleModel:
        """Look one page of the schedule up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                from_,
                last_seen=last_seen,
                timezone=timezone,
                groups_per_page=groups_per_page,
                items_per_group=items_per_group,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        from_: datetime | None = None,
        *,
        last_seen: str | None = None,
        timezone: str | None = None,
        groups_per_page: int = GROUPS_PER_PAGE,
        items_per_group: int = ITEMS_PER_GROUP,
    ) -> str:
        """Download one page of the schedule file.

        Args:
            from_: The day the page starts on. To match the website it is the
                first day of a month at 00:00:00. Left out the API answers from
                the current date.
            last_seen: The token the page before this one handed back. The
                website pages with this instead of `from_`, even when the next
                page runs into another month.
            timezone: The timezone the days are written in.
            groups_per_page: How many days one page covers.
            items_per_group: How many releases one day carries.
        """
        log_id = self.get_log_id(self.download, locals())
        params: dict[str, Any] = {
            "timezone": timezone or self._client.timezone,
            "groupsPerPage": groups_per_page,
            "itemsPerGroup": items_per_group,
        }

        if from_:
            params["from"] = from_.strftime("%Y-%m-%dT%H:%M:%S")

        if last_seen:
            params["lastSeen"] = last_seen

        return self._client.download(
            f"{BASE_API_URL}/api/v1/view/schedule",
            params=params,
            log_id=log_id,
        )

    # TODO: Validate
    def download_all(
        self,
        from_: datetime | None = None,
        *,
        timezone: str | None = None,
        groups_per_page: int = GROUPS_PER_PAGE,
        items_per_group: int = ITEMS_PER_GROUP,
    ) -> list[str]:
        """Download every page of the schedule from `from_` onwards."""
        pages: list[str] = []
        last_seen: str | None = None

        while True:
            page = self.download(
                from_ if not pages else None,
                last_seen=last_seen,
                timezone=timezone,
                groups_per_page=groups_per_page,
                items_per_group=items_per_group,
            )
            pages.append(page)
            last_seen = self.next_page_token(page)
            if not last_seen:
                return pages

    # TODO: Validate
    def download_merged(
        self,
        from_: datetime | None = None,
        *,
        timezone: str | None = None,
        groups_per_page: int = GROUPS_PER_PAGE,
        items_per_group: int = ITEMS_PER_GROUP,
    ) -> str:
        """Download the whole schedule from `from_` onwards as a single file.

        The pages are put together into one file holding every group, which is
        the whole schedule written the way one page of it is, rather than the
        pages themselves.
        """
        return self.merge_pages(
            self.download_all(
                from_,
                timezone=timezone,
                groups_per_page=groups_per_page,
                items_per_group=items_per_group,
            ),
        )

    # TODO: Validate
    @staticmethod
    def merge_pages(pages: list[str]) -> str:
        """Return the pages of one schedule written out as a single file.

        The first page is what the merged file is built on, since its layout and
        its other elements are what the schedule is, and the groups of its group
        list are replaced by the groups of every page in the order they were
        served. Each page covers the days after the one before it, so no group
        is listed twice. The actions are dropped: they ask for the page after a
        walk that is over, and a file holding the whole schedule is not a page
        of anything.

        Raises:
            ValueError: If there are no pages, since there is nothing to say the
                schedule was answered with.
        """
        if not pages:
            msg = "Expected at least one page, got none."
            raise ValueError(msg)

        def group_list(document: dict[str, Any]) -> dict[str, Any]:
            attributes: dict[str, Any] = next(
                element["attributes"]
                for element in document["elements"]
                if element["$type"] == "groupList"
            )
            return attributes

        documents: list[dict[str, Any]] = [json.loads(page) for page in pages]
        merged = json.loads(pages[0])
        merged_group_list = group_list(merged)
        merged_group_list["groups"] = [
            group for document in documents for group in group_list(document)["groups"]
        ]
        merged_group_list.pop("actions", None)
        return json.dumps(merged)

    # TODO: Validate
    @staticmethod
    def next_page_token(response: str) -> str | None:
        """Return what the next page is asked for, or None on the last page."""
        elements = json.loads(response)["elements"]
        group_list = next(
            element["attributes"]
            for element in elements
            if element["$type"] == "groupList"
        )
        # The last page has nothing to go to next, so it carries no actions at
        # all rather than an empty one.
        actions = group_list.get("actions")
        if not actions:
            return None
        token: str = actions["next"]["data"]["lastSeen"]
        return token

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ScheduleModel:
        """Read a downloaded schedule file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)

    # TODO: Validate
    def load_pages(self, pages: list[str]) -> list[ScheduleModel]:
        """Read the pages `download_all` returns into their models."""
        return [self.load(page) for page in pages]
