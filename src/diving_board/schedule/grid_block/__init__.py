"""Schedule grid block extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.grid_block.model import ScheduleGridBlockModel


class ScheduleGridBlock(BaseExtractor[ScheduleGridBlockModel]):
    """Provides methods to manage the grid block element from schedule data."""

    @cached_property
    @override
    def _response_model(self) -> type[ScheduleGridBlockModel]:
        return ScheduleGridBlockModel
