from datetime import datetime
from typing import Any

from gapi import CustomField, CustomSerializer, GapiCustomizations

from diving_board.protocol import DivingBoardProtocol
from diving_board.schedule import models
from diving_board.schedule.group_list import models as group_list_models

SCHEDULE_CUSTOMIZATIONS = customizations = GapiCustomizations(
    custom_fields=[
        # No idea why this is detected as "AwareDatetime | None" when there are string
        # inputs. Might be a problem with gapi that I need to fix at a later time, but a
        # quick test added to gapi shows that it can correctly create a model with these
        # parameters with the correct input.
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
    ],
)

SCHEDULE_GROUP_LIST_CUSTOMIZATIONS = customizations = GapiCustomizations(
    custom_fields=[
        # No idea why this is detected as "AwareDatetime | None" when there
        # are string inputs.
        CustomField(
            class_name="Attributes6",
            field_name="text",
            new_field="text: AwareDatetime | str | None = None",
        ),
        # Need to overrride the default datetime format because these
        # datetimes are naive.
        CustomField(
            class_name="Attributes2",
            field_name="text",
            new_field="text: NaiveDatetime",
        ),
        CustomField(
            class_name="Group",
            field_name="id",
            new_field="id: NaiveDatetime",
        ),
    ],
    # All of the NaiveDatetime fields need custom serialization code because
    # they use an unusual format.
    custom_serializers=[
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
    ],
    custom_imports=[
        "from pydantic import NaiveDatetime",
        "from datetime import datetime",
    ],
)


class ScheduleMixin(DivingBoardProtocol):
    def download_schedule(
        self,
        groups_per_page: int = 7,
        items_per_group: int = 7,
        from_value: datetime | None = None,
        last_seen: str | None = None,
    ) -> dict[str, Any]:
        # The URL used for the api call can be found on the releases page:
        # https://www.hidive.com/releases
        # Example API URL:
        # https://dce-frontoffice.imggaming.com/api/v1/view/schedule?timezone=America%2FLos_Angeles&groupsPerPage=7&itemsPerGroup=7&

        endpoint = "api/v1/view/schedule"

        params: dict[str, str | int] = {
            "timezone": self.timezone,
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

        return self._download_api_request(endpoint, params)

    def parse_schedule(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> models.Schedule:
        if update:
            return self.parse_response(
                models.Schedule,
                data,
                "schedule",
                SCHEDULE_CUSTOMIZATIONS,
            )

        return models.Schedule.model_validate(data)

    def get_schedule(
        self,
        groups_per_page: int = 7,
        items_per_group: int = 7,
        from_value: datetime | None = None,
        last_seen: str | None = None,
    ) -> models.Schedule:
        response = self.download_schedule(
            groups_per_page=groups_per_page,
            items_per_group=items_per_group,
            from_value=from_value,
            last_seen=last_seen,
        )
        return self.parse_schedule(response)

    def get_schedule_until_datetime(
        self,
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
        last_seen = ""

        # Stop the user from doing something silly on accident
        if end_datetime is None:
            end_datetime = datetime.now().astimezone()

        while True:
            schedule = self.get_schedule(
                groups_per_page=groups_per_page,
                items_per_group=items_per_group,
                from_value=from_value,
                last_seen=last_seen,
            )
            from_value = None  # from is only for the first request
            all_schedules.append(schedule)

            group_list = self.extract_schedule_group_list(schedule)

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

    def extract_schedule_group_list(
        self,
        data: models.Schedule,
        *,
        update: bool = True,
    ) -> group_list_models.ScheduleGroupList:
        for element in data.elements:
            if element.field_type == "groupList":
                season_data = element.model_dump(
                    mode="json",
                    by_alias=True,
                    exclude_unset=True,
                )

                if update:
                    return self.parse_response(
                        group_list_models.ScheduleGroupList,
                        season_data,
                        "schedule/group_list",
                        SCHEDULE_GROUP_LIST_CUSTOMIZATIONS,
                    )

                return group_list_models.ScheduleGroupList.model_validate(season_data)

        msg = "No bucket season element found in season data"
        raise ValueError(msg)
