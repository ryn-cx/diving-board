"""Contains the ScheduleGroupList class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.group_list.models import ScheduleGroupListModel


class ScheduleGroupList(BaseExtractor[ScheduleGroupListModel]):
    """Extract the group list element from Schedule."""

    _response_model = ScheduleGroupListModel
