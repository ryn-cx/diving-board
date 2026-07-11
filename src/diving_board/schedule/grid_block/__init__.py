# TODO: Validate
"""Schedule grid block extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.grid_block.model import ScheduleGridBlockModel


class ScheduleGridBlock(BaseExtractor[ScheduleGridBlockModel]):
    """Extracts data from Schedule where field_type=gridBlock."""

    _response_model = ScheduleGridBlockModel
