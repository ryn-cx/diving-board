# TODO: Validate
"""Schedule group list extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.group_list.models import ScheduleGroupListModel


class ScheduleGroupList(BaseExtractor[ScheduleGroupListModel]):
    """Extracts data from Schedule where field_type=groupList."""

    _response_model = ScheduleGroupListModel
