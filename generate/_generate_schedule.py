from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from diving_board import DivingBoard
from generate.constants import GENERATOR_PATHS

MODEL_NAME = "ScheduleModel"
FIRST_PAGE = "first-page"
NEXT_PAGE = "next-page"


# TODO: Validate
def next_page_token(client: DivingBoard) -> str | None:
    """Return what the page after the recorded first page is asked for."""
    first_page = GENERATOR_PATHS.recorded_path(MODEL_NAME, FIRST_PAGE)
    return client.schedule.next_page_token(first_page.read_text())


# TODO: Validate
class ScheduleId(RecordingId[DivingBoard]):
    page: str

    # TODO: Validate
    def download(self, client: DivingBoard) -> str:
        if self.page == FIRST_PAGE:
            return client.schedule.download()
        return client.schedule.download(last_seen=next_page_token(client))


PAGES = load_ids(GENERATOR_PATHS, MODEL_NAME, ScheduleId)


# TODO: Validate
def generate_schedule(client: DivingBoard) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, PAGES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ScheduleId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_schedule(DivingBoard(build_client_automatically()))
