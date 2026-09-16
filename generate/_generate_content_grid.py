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
from diving_board.content_grid import (
    MOVIES_GRID_VIEW_CONFIG_ID,
    SERIES_GRID_VIEW_CONFIG_ID,
)
from generate.constants import GENERATOR_PATHS

MODEL_NAME = "ContentGridModel"
FIRST_PAGE = "first-page"
NEXT_PAGE = "next-page"
LAST_PAGE = "last-page"

GRID_VIEW_CONFIG_IDS = {
    "series": SERIES_GRID_VIEW_CONFIG_ID,
    "movies": MOVIES_GRID_VIEW_CONFIG_ID,
}


# TODO: Validate
class ContentGridId(RecordingId[DivingBoard]):
    grid: str
    page: str

    # TODO: Validate
    def download(self, client: DivingBoard) -> str:
        grid_view_config_id = GRID_VIEW_CONFIG_IDS[self.grid]
        if self.page == FIRST_PAGE:
            return client.content_grid.download(grid_view_config_id)
        if self.page == LAST_PAGE:
            return client.content_grid.download_all(grid_view_config_id)[-1]
        return client.content_grid.download(
            grid_view_config_id,
            last_seen=self.first_page_token(client),
        )

    # TODO: Validate
    def first_page_token(self, client: DivingBoard) -> str | None:
        """Return what the page after this grid's recorded first page is asked for."""
        first_page = GENERATOR_PATHS.recorded_path(
            MODEL_NAME,
            ContentGridId(grid=self.grid, page=FIRST_PAGE).recording_name(),
        )
        return client.content_grid.next_page_token(first_page.read_text())


PAGES = load_ids(GENERATOR_PATHS, MODEL_NAME, ContentGridId)


# TODO: Validate
def generate_content_grid(client: DivingBoard) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, PAGES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ContentGridId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_content_grid(DivingBoard(build_client_automatically()))
