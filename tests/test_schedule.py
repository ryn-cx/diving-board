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
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_grid_block(data)

    def test_extract_filter_list(self, endpoint: Schedule) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_filter_list(data)

    def test_extract_group_list(self, endpoint: Schedule) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_group_list(data)

    def test_compile_entries(self, endpoint: Schedule) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            entries = endpoint.compile_cards(data)
            group_list = endpoint.extract_group_list(data)
            expected = [
                card
                for group in group_list.attributes.groups
                for card in group.attributes.cards
            ]
            assert entries == expected

    def test_compile_entries_from_list(self, endpoint: Schedule) -> None:
        data_list = [
            endpoint.parse(json.loads(f.read_text())) for f in endpoint.json_files()
        ]
        entries = endpoint.compile_cards(data_list)
        expected = [
            card
            for data in data_list
            for group in endpoint.extract_group_list(data).attributes.groups
            for card in group.attributes.cards
        ]
        assert entries == expected
