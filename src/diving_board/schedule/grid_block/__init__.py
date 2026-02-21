"""Schedule grid block extractor."""

from __future__ import annotations

from typing import override

from good_ass_pydantic_integrator import CustomSerializer, ReplacementType

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.grid_block.model import ScheduleGridBlockModel


class ScheduleGridBlock(BaseExtractor[ScheduleGridBlockModel]):
    """Extracts data from Schedule where field_type=gridBlock."""

    _response_model = ScheduleGridBlockModel

    @classmethod
    @override
    def _custom_serializers(cls) -> list[CustomSerializer]:
        return [cls._naive_datetime_serializer("Data", "from_")]

    @classmethod
    @override
    def _additional_imports(cls) -> list[str]:
        return ["from pydantic import NaiveDatetime"]

    @classmethod
    @override
    def _replacement_types(cls) -> list[ReplacementType]:
        return [
            ReplacementType(
                class_name="Data",
                field_name="from_",
                new_type="NaiveDatetime",
            ),
        ]
