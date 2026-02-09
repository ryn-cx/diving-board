"""Schedule API endpoint."""

from __future__ import annotations

from datetime import datetime
from functools import cached_property
from typing import Any, override

from gapi import CustomSerializer, ReplacementField

from diving_board.base_api_endpoint import BaseEndpoint, BaseExtractor
from diving_board.schedule import models
from diving_board.schedule.group_list import models as group_list_models


class Schedule(BaseEndpoint[models.Schedule]):
    """Provides methods to download, parse, and retrieve schedule data."""

    @cached_property
    @override
    def _response_model(self) -> type[models.Schedule]:
        """Return the Pydantic model class for this client."""
        return models.Schedule

    @cached_property
    @override
    def _custom_fields(self) -> list[ReplacementField]:
        # Need to override the default datetime format because these
        # datetimes are naive.
        return [
            ReplacementField(
                class_name="Attributes13",
                field_name="text",
                new_field="text: NaiveDatetime",
            ),
            ReplacementField(
                class_name="Group",
                field_name="id",
                new_field="id: NaiveDatetime",
            ),
            ReplacementField(
                class_name="Data",
                field_name="from_",
                new_field='from_: NaiveDatetime = Field(..., alias="from")',
            ),
        ]

    @cached_property
    @override
    def _custom_imports(self) -> list[str]:
        return ["from pydantic import NaiveDatetime"]

    # All of the NaiveDatetime fields need custom serialization code because
    # they use an unusual format.
    @cached_property
    @override
    def _custom_serializers(self) -> list[CustomSerializer]:
        return [
            CustomSerializer(
                class_name="Group",
                field_name="id",
                serializer_code='strf_string ="%Y-%m-%dT%H:%M"\n'
                "return value.strftime(strf_string)",
                input_type="NaiveDatetime",
                output_type="str",
            ),
            CustomSerializer(
                class_name="Attributes13",
                field_name="text",
                serializer_code='strf_string ="%Y-%m-%dT%H:%M"\n'
                "return value.strftime(strf_string)",
                input_type="NaiveDatetime",
                output_type="str",
            ),
            CustomSerializer(
                class_name="Data",
                field_name="from_",
                serializer_code='strf_string ="%Y-%m-%dT%H:%M"\n'
                "return value.strftime(strf_string)",
                input_type="NaiveDatetime",
                output_type="str",
            ),
        ]

    def download(
        self,
        groups_per_page: int = 7,
        items_per_group: int = 7,
        from_value: datetime | None = None,
        last_seen: str | None = None,
    ) -> dict[str, Any]:
        """Downloads schedule data.

        Args:
            groups_per_page: Number of groups per page.
            items_per_group: Number of items per group.
            from_value: Starting datetime for the schedule.
            last_seen: Pagination token from a previous response.

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
            "timezone": self._client.timezone,
            "groupsPerPage": groups_per_page,
            "itemsPerGroup": items_per_group,
        }

        # from_value is not present when getting airing episodes for the current month.
        if from_value:
            params["from"] = from_value.date().isoformat() + "T00:00:00"

        # last_seen is not present on the first page. For the most API consistent
        # results the value should be set to the first of the month like
        # 2026-06-01T00:00:00
        if last_seen:
            params["lastSeen"] = last_seen

        return self._client.download_api_request(endpoint, params)

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> models.Schedule:
        """Parses schedule data into a Schedule model.

        Args:
            data: The schedule data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A Schedule model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return models.Schedule.model_validate(data)

    def get(
        self,
        groups_per_page: int = 7,
        items_per_group: int = 7,
        from_value: datetime | None = None,
        last_seen: str | None = None,
    ) -> models.Schedule:
        """Downloads and parses schedule data.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            groups_per_page: Number of groups per page.
            items_per_group: Number of items per group.
            from_value: Starting datetime for the schedule.
            last_seen: Pagination token from a previous response.

        Returns:
            A Schedule model containing the parsed data.
        """
        response = self.download(
            groups_per_page=groups_per_page,
            items_per_group=items_per_group,
            from_value=from_value,
            last_seen=last_seen,
        )
        return self.parse(response)

    def get_until_datetime(
        self,
        groups_per_page: int = 7,
        items_per_group: int = 7,
        end_datetime: datetime | None = None,
        *,
        from_value: datetime | None = None,
    ) -> list[models.Schedule]:
        """Get all schedule pages until end_datetime is reached.

        Args:
            groups_per_page: Number of groups per page.
            items_per_group: Number of items per group.
            end_datetime: Stop when reaching this datetime.
            from_value: Starting datetime for the schedule.

        Returns:
            List of Schedule pages.
        """
        all_schedules: list[models.Schedule] = []
        last_seen = ""

        # Stop the user from doing something silly on accident
        if end_datetime is None:
            end_datetime = datetime.now().astimezone()

        while True:
            schedule = self.get(
                groups_per_page=groups_per_page,
                items_per_group=items_per_group,
                from_value=from_value,
                last_seen=last_seen,
            )
            from_value = None  # from is only for the first request
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

    def extract_group_list(
        self,
        data: models.Schedule,
        *,
        update: bool = True,
    ) -> group_list_models.GroupList:
        """Extract the group list element from schedule data.

        Args:
            data: Schedule data to extract from.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A ScheduleGroupList model containing the parsed data.
        """
        for element in data.elements:
            if element.field_type == "groupList":
                dumped_group_list = self._dump_response(element)
                return GroupList().parse(dumped_group_list, update=update)

        msg = "No groupList element found in schedule data"
        raise ValueError(msg)


class GroupList(BaseExtractor[group_list_models.GroupList]):
    """Provides methods to manage the group list element from schedule data."""

    @cached_property
    def _custom_fields(self) -> list[ReplacementField]:
        return [
            ReplacementField(
                class_name="Attributes6",
                field_name="text",
                new_field="text: NaiveDatetime | str | None = None",
            ),
            # Need to override the default datetime format because these
            # datetimes are naive.
            ReplacementField(
                class_name="Attributes2",
                field_name="text",
                new_field="text: NaiveDatetime",
            ),
            ReplacementField(
                class_name="Group",
                field_name="id",
                new_field="id: NaiveDatetime",
            ),
        ]

    @cached_property
    def _custom_imports(self) -> list[str]:
        return [
            "from pydantic import NaiveDatetime",
            "from datetime import datetime",
        ]

    # All of the NaiveDatetime fields need custom serialization code because
    # they use an unusual format.
    @cached_property
    def _custom_serializers(self) -> list[CustomSerializer]:
        return [
            CustomSerializer(
                class_name="Attributes2",
                field_name="text",
                serializer_code='strf_string ="%Y-%m-%dT%H:%M"\n'
                "return value.strftime(strf_string)",
                input_type="NaiveDatetime",
                output_type="str",
            ),
            CustomSerializer(
                class_name="Attributes6",
                field_name="text",
                serializer_code="if isinstance(value, (str, type(None))):\n"
                "    return value\n"
                'strf_string ="%Y-%m-%dT%H:%M"\n'
                "return value.strftime(strf_string)",
                input_type="AwareDatetime | str | None",
                output_type="str | None",
            ),
            CustomSerializer(
                class_name="Group",
                field_name="id",
                serializer_code='strf_string ="%Y-%m-%dT%H:%M"\n'
                "return value.strftime(strf_string)",
                input_type="NaiveDatetime",
                output_type="str",
            ),
        ]

    @cached_property
    @override
    def _response_model(self) -> type[group_list_models.GroupList]:
        """Return the Pydantic model class for this client."""
        return group_list_models.GroupList

    def parse(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> group_list_models.GroupList:
        """Parses group list data into a GroupList model.

        Args:
            data: The group list data to parse.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            A ScheduleGroupList model containing the parsed data.
        """
        if update:
            return self._parse_response(data)

        return group_list_models.GroupList.model_validate(data)

    @cached_property
    def _response_model_folder_name(self) -> str:
        """Return the snake_case version of the response model's class name."""
        return "schedule/" + super()._response_model_folder_name
