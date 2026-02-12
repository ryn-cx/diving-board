"""Schedule filter list extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.filter_list.model import ScheduleFilterListModel


class ScheduleFilterList(BaseExtractor[ScheduleFilterListModel]):
    """Provides methods to manage the filter list element from schedule data."""

    @cached_property
    @override
    def _response_model(self) -> type[ScheduleFilterListModel]:
        return ScheduleFilterListModel
