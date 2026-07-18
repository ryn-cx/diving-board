# TODO: Validate
from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.schedule import Schedule

NAME = "schedule"


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Schedule:
    return client.schedule


class TestSchedule:
    def test_download(self, endpoint: Schedule) -> None:
        download_and_save(endpoint, NAME, endpoint.download)

    def test_extract_grid_block(self, endpoint: Schedule) -> None:
        grid_block = endpoint.extract_grid_block(parse_json(endpoint, NAME))
        assert grid_block.attributes.elements

    def test_extract_filter_list(self, endpoint: Schedule) -> None:
        filter_list = endpoint.extract_filter_list(parse_json(endpoint, NAME))
        assert filter_list.attributes.filters

    def test_extract_group_list(self, endpoint: Schedule) -> None:
        group_list = endpoint.extract_group_list(parse_json(endpoint, NAME))
        assert group_list.attributes.groups

    def test_compile_cards(self, endpoint: Schedule) -> None:
        data = parse_json(endpoint, NAME)
        entries_from_file = endpoint.compile_cards(data)
        entries_from_list = endpoint.compile_cards([data])
        group_list = endpoint.extract_group_list(data)
        expected = [
            card
            for group in group_list.attributes.groups
            for card in group.attributes.cards
        ]
        assert entries_from_file == expected == entries_from_list

    def test_download_and_parse_until_datetime(self, endpoint: Schedule) -> None:
        end_datetime = datetime.now().astimezone() + timedelta(days=30)
        schedules = endpoint.download_and_parse_until_datetime(end_datetime)
        assert len(schedules) > 1

    def test_past_last_available_date(self, endpoint: Schedule) -> None:
        end_datetime = datetime.now().astimezone() + timedelta(days=365)
        schedules = endpoint.download_and_parse_until_datetime(
            end_datetime=end_datetime,
        )
        assert len(schedules) > 1


@pytest.mark.parametrize("last_seen", [None, "token"])
def test_log_id(endpoint: Schedule, last_seen: str | None) -> None:
    expected = "Schedule from_=None"
    if last_seen is not None:
        expected += f" last_seen={last_seen!r}"
    assert endpoint.get_log_id(last_seen=last_seen) == expected
