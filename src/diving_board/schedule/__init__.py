from datetime import datetime
from typing import Any

from gapi import CustomField, CustomSerializer, GapiCustomizations

from diving_board.protocol import DivingBoardProtocol
from diving_board.schedule import models
from diving_board.schedule.group_list import models as group_list_models

CUSTOMIZATIONS = customizations = GapiCustomizations(
    custom_fields=[
        # No idea why this is detected as "AwareDatetime | None" when there
        # are string inputs.
        CustomField(
            class_name="Attributes17",
            field_name="text",
            new_field="text: AwareDatetime | str | None = None",
        ),
        # Need to overrride the default datetime format because these
        # datetimes are naive.
        CustomField(
            class_name="Attributes13",
            field_name="text",
            new_field="text: NaiveDatetime",
        ),
        CustomField(
            class_name="Group",
            field_name="id",
            new_field="id: NaiveDatetime",
        ),
        CustomField(
            class_name="Data",
            field_name="from_",
            new_field='from_: NaiveDatetime = Field(..., alias="from")',
        ),
    ],
    custom_imports=[
        "from pydantic import NaiveDatetime",
    ],
    # All of the NaiveDatetime fields need custom serialization code because
    # they use an unusual format.
    custom_serializers=[
        CustomSerializer(
            class_name="Group",
            field_name="id",
            serializer_code='strf_string ="%Y-%m-%dT%H:%M"\n'
            "return value.strftime(strf_string)",
        ),
        CustomSerializer(
            class_name="Attributes13",
            field_name="text",
            serializer_code='strf_string ="%Y-%m-%dT%H:%M"\n'
            "return value.strftime(strf_string)",
        ),
        CustomSerializer(
            class_name="Data",
            field_name="from_",
            serializer_code='strf_string ="%Y-%m-%dT%H:%M"\n'
            "return value.strftime(strf_string)",
        ),
    ],
)


class ScheduleMixin(DivingBoardProtocol):
    def download_schedule(
        self,
        timezone: str = "America/Los_Angeles",
        groups_per_page: int = 7,
        items_per_group: int = 7,
        from_value: datetime | None = None,
        last_seen: str | None = None,
    ) -> dict[str, Any]:
        params: dict[str, str | int] = {
            "timezone": timezone,
            "groupsPerPage": groups_per_page,
            "itemsPerGroup": items_per_group,
        }

        if from_value:
            params["from"] = from_value.date().isoformat() + "T00:00:00"

        if last_seen:
            params["lastSeen"] = last_seen

        return self._get_api_request("api/v1/view/schedule", params=params)

    def parse_schedule(
        self,
        data: dict[str, Any],
        *,
        update: bool = False,
    ) -> models.Schedule:
        if update:
            return self.parse_response(
                models.Schedule,
                data,
                "schedule",
                CUSTOMIZATIONS,
            )

        return models.Schedule.model_validate(data)

    def get_schedule(
        self,
        timezone: str = "America/Los_Angeles",
        groups_per_page: int = 7,
        items_per_group: int = 7,
        from_value: datetime | None = None,
        last_seen: str | None = None,
    ) -> models.Schedule:
        data = self.download_schedule(
            timezone=timezone,
            groups_per_page=groups_per_page,
            items_per_group=items_per_group,
            from_value=from_value,
            last_seen=last_seen,
        )
        return self.parse_schedule(data, update=True)

    # TODO: Deprecate?
    def extract_schedule_vods(
        self,
        data: models.Schedule
        | list[models.Schedule]
        | dict[str, Any]
        | list[dict[str, Any]],
    ) -> list[models.Data5]:
        if isinstance(data, list):
            vods: list[models.Data5] = []
            for schedule in data:
                vods.extend(self.extract_schedule_vods(schedule))
            return vods

        if isinstance(data, dict):
            data = self.parse_response(
                models.Schedule,
                data,
                "schedule",
                CUSTOMIZATIONS,
            )

        # ruff says this is the best way even though it's impossible to read...
        return [
            card_wrapper.attributes.action.data
            for element in data.elements
            for group in element.attributes.groups or []
            for card_wrapper in group.attributes.cards
            if card_wrapper.attributes.action.data.type == "VOD"
        ]

    def get_schedule_until_datetime(
        self,
        timezone: str = "America/Los_Angeles",
        groups_per_page: int = 7,
        items_per_group: int = 7,
        end_datetime: datetime | None = None,
        *,
        from_value: datetime | None = None,
    ) -> list[models.Schedule]:
        """Get all schedule pages until end_datetime is reached.

        Args:
            timezone: Timezone for schedule
            groups_per_page: Number of groups per page
            items_per_group: Number of items per group
            from_value: Starting datetime
            end_datetime: Stop when reaching this datetime

        Returns:
            List of Schedule pages
        """
        all_schedules: list[models.Schedule] = []
        last_seen: str | None = None

        # Stop the user from doing something silly on accident
        if end_datetime is None:
            end_datetime = datetime.now().astimezone()

        while True:
            result = self.get_schedule(
                timezone=timezone,
                groups_per_page=groups_per_page,
                items_per_group=items_per_group,
                from_value=from_value,
                last_seen=last_seen,
            )
            from_value = None  # from is only for the first request
            all_schedules.append(result)

            # TODO: Nasty ass code
            last_seen = None
            for element in result.elements:
                if (
                    element.attributes.actions
                    and element.attributes.actions.next
                    and element.attributes.actions.next.data.last_seen
                ):
                    last_seen = element.attributes.actions.next.data.last_seen

            if last_seen is None:
                return all_schedules

            # The order of the entries is sometimes really weird where an upcoming
            # episode from months in the future will be mixed into the upcoming releases
            # so wait until all videos are past the end_datetime value.
            videos = self.extract_schedule_vods(result)
            if videos and all(
                video.computed_releases[0].scheduled_at >= end_datetime
                for video in videos
            ):
                return all_schedules

    def extract_schedule_group_list(
        self,
        data: models.Schedule,
        *,
        update: bool = False,
    ) -> group_list_models.ScheduleGroupList:
        for element in data.elements:
            if element.field_type == "groupList":
                season_data = element.model_dump(mode="json")

                if update:
                    return self.parse_response(
                        group_list_models.ScheduleGroupList,
                        season_data,
                        "schedule/group_list",
                    )

                return group_list_models.ScheduleGroupList.model_validate(season_data)

        msg = "No bucket season element found in season data"
        raise ValueError(msg)
