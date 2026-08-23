# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.schedule import GROUPS_PER_PAGE
from diving_board.schedule.models import ScheduleModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from diving_board import DivingBoard

FIRST_PAGE = "first-page"
NEXT_PAGE = "next-page"

PAGES = [
    pytest.param(FIRST_PAGE, id="first page"),
    pytest.param(NEXT_PAGE, id="page after the first"),
]


class ScheduleTest(RecordedEndpoint):
    MODEL = ScheduleModel


# TODO: Validate
def days(schedule: ScheduleModel) -> int:
    """Return how many days the page covers."""
    groups = next(
        element.attributes.groups
        for element in schedule.elements or []
        if element.field_type == "groupList"
    )
    return len(groups or [])


# TODO: Validate
def test_download(client: DivingBoard) -> None:
    ScheduleTest.download_test(FIRST_PAGE, client.schedule.download)


# TODO: Validate
def test_download_next_page(client: DivingBoard) -> None:
    # The site pages the schedule by the token the page before it handed back
    # rather than by date.
    last_seen = client.schedule.next_page_token(
        ScheduleTest.recorded_content(FIRST_PAGE),
    )
    ScheduleTest.download_test(
        NEXT_PAGE,
        lambda: client.schedule.download(last_seen=last_seen),
    )


# TODO: Validate
@pytest.mark.parametrize("page", PAGES)
def test_parse(client: DivingBoard, page: str) -> None:
    data = client.schedule.load(ScheduleTest.recorded_content(page))
    assert days(data) == GROUPS_PER_PAGE
