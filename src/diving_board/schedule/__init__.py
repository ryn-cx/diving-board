"""Schedule API endpoint."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, override

from good_ass_pydantic_integrator import CustomSerializer, ReplacementType

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.schedule.filter_list import ScheduleFilterList
from diving_board.schedule.grid_block import ScheduleGridBlock
from diving_board.schedule.group_list import ScheduleGroupList
from diving_board.schedule.models import ScheduleModel

if TYPE_CHECKING:
    from diving_board.schedule.filter_list.model import ScheduleFilterListModel
    from diving_board.schedule.grid_block.model import ScheduleGridBlockModel
    from diving_board.schedule.group_list.models import ScheduleGroupListModel


class Schedule(BaseEndpoint[ScheduleModel]):
    """Provides methods to download, parse, and retrieve schedule data."""

    _response_model = ScheduleModel

    @classmethod
    @override
    def _replacement_types(cls) -> list[ReplacementType]:
        return [
            ReplacementType(
                class_name="Attributes13",
                field_name="text",
                new_type="NaiveDatetime",
            ),
            ReplacementType(
                class_name="Group",
                field_name="id",
                new_type="NaiveDatetime",
            ),
            ReplacementType(
                class_name="Data",
                field_name="from_",
                new_type="NaiveDatetime",
            ),
        ]

    @classmethod
    @override
    def _additional_imports(cls) -> list[str]:
        return ["from pydantic import NaiveDatetime"]

    @classmethod
    @override
    def _custom_serializers(cls) -> list[CustomSerializer]:
        return [
            cls._naive_datetime_serializer("Group", "id"),
            cls._naive_datetime_serializer("Attributes13", "text"),
            cls._naive_datetime_serializer("Data", "from_"),
        ]

    def download(
        self,
        from_: datetime | None = None,
        last_seen: str | None = None,
        groups_per_page: int = 7,
        items_per_group: int = 7,
        timezone: str = "",
    ) -> dict[str, Any]:
        """Downloads schedule data for a given datetime and pagination token.

        Args:
            groups_per_page: Number of groups per page.
            items_per_group: Number of items per group.
            from_: Starting datetime for the schedule, to match the API used by the
                website it should be the first day of a month at a time of 00:00:00.
            last_seen: Pagination token from a previous response.
            timezone: The timezone to use for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        # Example request headers from: https://www.hidive.com/releases
        """GET /api/v1/view/schedule
                ?timezone=America%2FLos_Angeles&groupsPerPage=7&itemsPerGroup=7& HTTP/2
            Host: dce-frontoffice.imggaming.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0)
                        Gecko/20100101 Firefox/147.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US
            Accept-Encoding: gzip, deflate, br, zstd
            Referer: https://www.hidive.com/
            Content-Type: application/json
            x-api-key: 857a1e5d-e35e-4fdf-805b-a87b6f8364bf
            app: dice
            Realm: dce.hidive
            x-app-var: 6.60.0.ae5c96d
            Authorization: Bearer TOKEN
            Origin: https://www.hidive.com
            Connection: keep-alive
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: cross-site
            Priority: u=4
            TE: trailers"""
        endpoint = "api/v1/view/schedule"

        params: dict[str, str | int] = {
            "timezone": timezone or self._client.timezone,
            "groupsPerPage": groups_per_page,
            "itemsPerGroup": items_per_group,
        }

        # from is not used when getting results from the current month so it should be
        # an optional parameter.
        if from_:
            params["from"] = from_.date().isoformat() + "T00:00:00"

        # last_seen is not present on the first page so it should be optional parameter.
        if last_seen:
            params["lastSeen"] = last_seen

        return self._client.download(endpoint, params)

    def get(
        self,
        from_: datetime | None = None,
        last_seen: str | None = None,
        groups_per_page: int = 7,
        items_per_group: int = 7,
        timezone: str = "",
    ) -> ScheduleModel:
        """Downloads and parses schedule data.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            groups_per_page: Number of groups per page.
            items_per_group: Number of items per group.
            from_: Starting datetime for the schedule, to match the API used by the
                website it should be the first day of a month at a time of 00:00:00.
            last_seen: Pagination token from a previous response.
            timezone: The timezone to use for the request.

        Returns:
            A Schedule model containing the parsed data.
        """
        response = self.download(
            groups_per_page=groups_per_page,
            items_per_group=items_per_group,
            from_=from_,
            last_seen=last_seen,
            timezone=timezone,
        )
        return self.parse(response)

    def get_until_datetime(
        self,
        from_: datetime | None = None,
        end_datetime: datetime | None = None,
        groups_per_page: int = 7,
        items_per_group: int = 7,
        timezone: str = "",
    ) -> list[ScheduleModel]:
        """Get all schedule pages until end_datetime is reached.

        Args:
            groups_per_page: Number of groups per page.
            items_per_group: Number of items per group.
            from_: Starting datetime for the schedule, to match the API used by the
                website it should be the first day of a month at a time of 00:00:00.
            end_datetime: Stop when a release for this date or later is found.
            timezone: The timezone to use for the request.

        Returns:
            List of Schedule pages.
        """
        all_schedules: list[ScheduleModel] = []
        last_seen = ""

        # If no end_datetime is given assume the user wants everything up to the current
        # date for simplicity.
        if end_datetime is None:
            end_datetime = datetime.now().astimezone()

        while True:
            schedule = self.get(
                groups_per_page=groups_per_page,
                items_per_group=items_per_group,
                from_=from_,
                last_seen=last_seen,
                timezone=timezone,
            )
            # When using the website from is only sent on the first request for a
            # specific month. After that everything just uses lastSeen even if the
            # results come from future months so the argument can be removed.
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
        """Extract the grid block element from schedule data.

        Args:
            data: Schedule data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A ScheduleGridBlockModel containing the parsed data.
        """
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
        """Extract the filter list element from schedule data.

        Args:
            data: Schedule data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A ScheduleFilterListModel containing the parsed data.
        """
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
        """Extract the group list element from schedule data.

        Args:
            data: Schedule data to extract from.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A ScheduleGroupListModel containing the parsed data.
        """
        return self._extract_element(
            data.elements,
            "groupList",
            ScheduleGroupList,
            update_model=update_model,
        )
