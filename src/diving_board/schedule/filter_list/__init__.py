"""Schedule filter list extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.schedule.filter_list.model import ScheduleFilterListModel


class ScheduleFilterList(BaseExtractor[ScheduleFilterListModel]):
    """Extracts data from Schedule where field_type=filterList."""

    _response_model = ScheduleFilterListModel
