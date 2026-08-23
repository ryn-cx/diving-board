# TODO: Validate
"""Rebuilds ScheduleModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from diving_board import DivingBoard
from generate.constants import DIVING_BOARD_PATH, FILES_PATH
from generate.utils import download_if_missing

FIRST_PAGE = "first-page"
NEXT_PAGE = "next-page"


# TODO: Validate
def next_page_token(client: DivingBoard) -> str | None:
    """Return what the page after the recorded first page is asked for."""
    first_page = FILES_PATH / "ScheduleModel" / f"{FIRST_PAGE}.json"
    return client.schedule.next_page_token(first_page.read_text())


# TODO: Validate
def generate_schedule(client: DivingBoard) -> None:
    """Rebuild ScheduleModel."""
    download_if_missing(
        FILES_PATH,
        "ScheduleModel",
        FIRST_PAGE,
        client.schedule.download,
    )
    download_if_missing(
        FILES_PATH,
        "ScheduleModel",
        NEXT_PAGE,
        lambda: client.schedule.download(last_seen=next_page_token(client)),
    )
    generate_model(FILES_PATH, DIVING_BOARD_PATH, "ScheduleModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_schedule(DivingBoard(build_client_automatically()))
