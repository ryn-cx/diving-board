"""Contains the ScheduleGridBlock class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.grid_block.models import ScheduleGridBlockModel


class ScheduleGridBlock(BaseExtractor[ScheduleGridBlockModel]):
    """Extract the grid block element from Schedule."""

    _response_model = ScheduleGridBlockModel
