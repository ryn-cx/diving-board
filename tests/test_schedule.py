# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from diving_board.schedule import GROUPS_PER_PAGE

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.schedule.models import ScheduleModel


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
    assert days(client.schedule()) == GROUPS_PER_PAGE


# TODO: Validate
def test_download_next_page(client: DivingBoard) -> None:
    # The site pages the schedule by the token the page before it handed back
    # rather than by date.
    last_seen = client.schedule.next_page_token(client.schedule.download())
    assert days(client.schedule(last_seen=last_seen)) == GROUPS_PER_PAGE
