"""Contains the Schedule class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.constants import BASE_API_URL
from diving_board.schedule.filter_list import ScheduleFilterList
from diving_board.schedule.grid_block import ScheduleGridBlock
from diving_board.schedule.group_list import ScheduleGroupList
from diving_board.schedule.models import ScheduleModel

if TYPE_CHECKING:
    from datetime import datetime

    from diving_board.schedule.filter_list.model import ScheduleFilterListModel
    from diving_board.schedule.grid_block.model import ScheduleGridBlockModel
    from diving_board.schedule.group_list.models import ScheduleGroupListModel


class Schedule(BaseEndpoint[ScheduleModel]):
    """Manage the schedule file."""

    _response_model = ScheduleModel

    def download(
        self,
        from_: datetime | None = None,
        last_seen: str | None = None,
        timezone: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the schedule file.

        Args:
            from_: Starting datetime for the schedule, to match the API used by the
                website it should be the first day of a month at a time of 00:00:00. If
                no value is given it will default to the current date.
            last_seen: Pagination token from a previous response.
            timezone: The timezone to use for the request.

        Example request: https://www.hidive.com/releases
            OPTIONS /api/v1/view/schedule?timezone=America%2FLos_Angeles&groupsPerPage=7&itemsPerGroup=7& HTTP/2
            Host: dce-frontoffice.imggaming.com
            User-Agent: __REDACTED__
            Accept: */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Access-Control-Request-Method: GET
            Access-Control-Request-Headers: app,authorization,content-type,realm,x-api-key,x-app-var
            Referer: https://www.hidive.com/
            Origin: https://www.hidive.com
            Connection: keep-alive
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: cross-site
            Priority: u=4

        Example request: https://www.hidive.com/releases -> click next/previous month.
            GET /api/v1/view/schedule?timezone=America%2FLos_Angeles&groupsPerPage=7&itemsPerGroup=7&&from=2026-06-01T00%3A00%3A00 HTTP/2
            Host: dce-frontoffice.imggaming.com
            User-Agent: __REDACTED__
            Accept: application/json, text/plain, */*
            Accept-Language: en-US
            Accept-Encoding: gzip, deflate, br, zstd
            Referer: https://www.hidive.com/
            Content-Type: application/json
            x-api-key: 857a1e5d-e35e-4fdf-805b-a87b6f8364bf
            app: dice
            Realm: dce.hidive
            x-app-var: 6.60.0.5aaf921
            Authorization: Bearer __REDACTED__
            Origin: https://www.hidive.com
            Connection: keep-alive
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: cross-site
            Priority: u=0
            TE: trailers
        """
        params: dict[str, str | int] = {
            "timezone": timezone or self._client.timezone,
            "groupsPerPage": 7,
            "itemsPerGroup": 7,
        }

        # from is not used to get the schedule from the current date.
        if from_:
            params["from"] = from_.strftime("%Y-%m-%dT%H:%M:%S")

        # last_seen is not used on the first page.
        if last_seen:
            params["lastSeen"] = last_seen

        return self._client.download(
            f"{BASE_API_URL}/api/v1/view/schedule",
            params,
            f"{self.__class__.__name__} {[from_, last_seen]}",
        )

    def get(
        self,
        from_: datetime | None = None,
        last_seen: str | None = None,
        timezone: str | None = None,
    ) -> ScheduleModel:
        """Downloads and parses the schedule file.

        Args:
            from_: Starting datetime for the schedule, to match the API used by the
                website it should be the first day of a month at a time of 00:00:00. If
                no value is given it will default to the current date.
            last_seen: Pagination token from a previous response.
            timezone: The timezone to use for the request.
        """
        response = self.download(
            from_=from_,
            last_seen=last_seen,
            timezone=timezone,
        )
        return self.parse(response)

    def get_until_datetime(
        self,
        end_datetime: datetime,
        from_: datetime | None = None,
        timezone: str | None = None,
    ) -> list[ScheduleModel]:
        """Get all schedule files until end_datetime is reached (inclusive).

        Args:
            from_: Starting datetime for the schedule, to match the API used by the
                website it should be the first day of a month at a time of 00:00:00. If
                no value is given it will default to the current date.
            end_datetime: Stop when all releases before this date are found.
            timezone: The timezone to use for the request.
        """
        all_schedules: list[ScheduleModel] = []
        last_seen = ""

        while True:
            schedule = self.get(from_=from_, last_seen=last_seen, timezone=timezone)
            # When using the website from is only sent on the first request for a
            # specific month. After that everything uses lastSeen even if the results
            # come from future months so the argument can be removed
            from_ = None
            all_schedules.append(schedule)

            group_list = self.extract_group_list(schedule)

            if group_list.attributes.actions:
                last_seen = group_list.attributes.actions.next.data.last_seen
            else:
                return all_schedules

            # The order of the entries is sometimes really weird where an upcoming
            # episode from months in the future will be mixed into the upcoming releases
            # so wait until all videos are past the end_datetime value.
            if all(
                video.attributes.title.attributes.text.astimezone() >= end_datetime
                for video in group_list.attributes.groups
            ):
                return all_schedules

    def extract_grid_block(
        self,
        data: ScheduleModel,
        *,
        update_model: bool = True,
    ) -> ScheduleGridBlockModel:
        """Extract the grid block element from Schedule."""
        return self._extract_element(
            data.elements,
            "gridBlock",
            ScheduleGridBlock,
            update_model=update_model,
        )

    def extract_filter_list(
        self,
        data: ScheduleModel,
        *,
        update_model: bool = True,
    ) -> ScheduleFilterListModel:
        """Extract the filter list element from Schedule."""
        return self._extract_element(
            data.elements,
            "filterList",
            ScheduleFilterList,
            update_model=update_model,
        )

    def extract_group_list(
        self,
        data: ScheduleModel,
        *,
        update_model: bool = True,
    ) -> ScheduleGroupListModel:
        """Extract the group list element from Schedule."""
        return self._extract_element(
            data.elements,
            "groupList",
            ScheduleGroupList,
            update_model=update_model,
        )
