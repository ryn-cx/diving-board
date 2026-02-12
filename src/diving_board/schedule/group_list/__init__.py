"""Schedule group list extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from gapi import CustomSerializer, ReplacementField

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.group_list.models import ScheduleGroupListModel


class ScheduleGroupList(BaseExtractor[ScheduleGroupListModel]):
    """Provides methods to manage the group list element from schedule data."""

    @cached_property
    @override
    def _replacement_fields(self) -> list[ReplacementField]:
        return [
            ReplacementField(
                class_name="Attributes6",
                field_name="text",
                new_field="text: NaiveDatetime | str | None = None",
            ),
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
    @override
    def _additional_imports(self) -> list[str]:
        return [
            "from pydantic import NaiveDatetime",
            "from datetime import datetime",
        ]

    # All of the NaiveDatetime fields need custom serialization code because
    # they use an unusual format.
    @cached_property
    @override
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
    def _response_model(self) -> type[ScheduleGroupListModel]:
        return ScheduleGroupListModel
