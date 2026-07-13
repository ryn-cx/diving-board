"""Contains the ScheduleFilterList class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.filter_list.models import ScheduleFilterListModel


class ScheduleFilterList(BaseExtractor[ScheduleFilterListModel]):
    """Extract the filter list element from Schedule."""

    _response_model = ScheduleFilterListModel
