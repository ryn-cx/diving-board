from __future__ import annotations

import json
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

import pytest

from tests.utils import data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from diving_board import DivingBoard
    from diving_board.schedule import Schedule
    from diving_board.schedule.models import ScheduleModel

NAME = "schedule"


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Schedule:
    return client.schedule


@pytest.fixture(scope="session")
def json_file(endpoint: Schedule) -> Path:
    return data_path(endpoint, NAME)


@pytest.fixture(scope="session")
def data(endpoint: Schedule, json_file: Path) -> ScheduleModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSchedule:
    def test_download(self, endpoint: Schedule) -> None:
        download_if_missing(endpoint, NAME, endpoint.download)

    def test_extract_grid_block(self, endpoint: Schedule, data: ScheduleModel) -> None:
        grid_block = endpoint.extract_grid_block(data)
        assert grid_block.attributes.elements

    def test_extract_filter_list(self, endpoint: Schedule, data: ScheduleModel) -> None:
        filter_list = endpoint.extract_filter_list(data)
        assert filter_list.attributes.filters

    def test_extract_group_list(self, endpoint: Schedule, data: ScheduleModel) -> None:
        group_list = endpoint.extract_group_list(data)
        assert group_list.attributes.groups

    def test_compile_cards(self, endpoint: Schedule, data: ScheduleModel) -> None:
        entries_from_file = endpoint.compile_cards(data)
        entries_from_list = endpoint.compile_cards([data])
        group_list = endpoint.extract_group_list(data)
        expected = [
            card
            for group in group_list.attributes.groups
            for card in group.attributes.cards
        ]
        assert entries_from_file == expected == entries_from_list

    def test_get_until_datetime(self, endpoint: Schedule) -> None:
        end_datetime = datetime.now().astimezone() + timedelta(days=30)
        schedules = endpoint.get_until_datetime(end_datetime)
        assert len(schedules) > 1

    def test_get_past_last_available_date(self, endpoint: Schedule) -> None:
        end_datetime = datetime.now().astimezone() + timedelta(days=365)
        schedules = endpoint.get_until_datetime(end_datetime=end_datetime)
        assert len(schedules) > 1
