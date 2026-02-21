"""Schedule group list extractor."""

from __future__ import annotations

from typing import override

from good_ass_pydantic_integrator import CustomSerializer, ReplacementType

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.group_list.models import ScheduleGroupListModel


class ScheduleGroupList(BaseExtractor[ScheduleGroupListModel]):
    """Extracts data from Schedule where field_type=groupList."""

    _response_model = ScheduleGroupListModel

    @classmethod
    @override
    def _replacement_types(cls) -> list[ReplacementType]:
        return [
            ReplacementType(
                class_name="Attributes2",
                field_name="text",
                new_type="NaiveDatetime",
            ),
            ReplacementType(
                class_name="Group",
                field_name="id",
                new_type="NaiveDatetime",
            ),
        ]

    @classmethod
    @override
    def _additional_imports(cls) -> list[str]:
        return [
            "from pydantic import NaiveDatetime",
            "from datetime import datetime",
        ]

    @classmethod
    @override
    def _custom_serializers(cls) -> list[CustomSerializer]:
        return [
            cls._naive_datetime_serializer("Attributes2", "text"),
            cls._naive_datetime_serializer("Group", "id"),
        ]
