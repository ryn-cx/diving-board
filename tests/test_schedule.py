from __future__ import annotations

import json
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.schedule import Schedule


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Schedule:
    return client.schedule


class TestSchedule:
    def test_get(self, endpoint: Schedule) -> None:
        data = endpoint.get()
        assert data.elements
        endpoint.save_new_json_file(endpoint.original_input(data))

    def test_get_from(self, endpoint: Schedule) -> None:
        first_of_month = (
            datetime.now()
            .astimezone()
            .replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        )

        data = endpoint.get(first_of_month)
        assert data.elements
        endpoint.save_new_json_file(endpoint.original_input(data))

    def test_get_until_datetime(self, endpoint: Schedule) -> None:
        end_datetime = datetime.now().astimezone() + timedelta(days=30)
        schedules = endpoint.get_until_datetime(end_datetime)
        assert len(schedules) > 1

    def test_get_past_last_available_date(self, endpoint: Schedule) -> None:
        end_datetime = datetime.now().astimezone() + timedelta(days=365)
        schedules = endpoint.get_until_datetime(end_datetime=end_datetime)
        assert len(schedules) > 1

    def test_parse(self, endpoint: Schedule) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_grid_block(self, endpoint: Schedule) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_grid_block(model)

    def test_extract_filter_list(self, endpoint: Schedule) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_filter_list(model)

    def test_extract_group_list(self, endpoint: Schedule) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_group_list(model)
