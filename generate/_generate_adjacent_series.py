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

MODEL_NAME = "AdjacentSeriesModel"


# TODO: Validate
class AdjacentSeriesId(RecordingId[DivingBoard]):
    series_id: int
    season_id: int

    # TODO: Validate
    def download(self, client: DivingBoard) -> str:
        return client.adjacent_series.download(self.series_id, self.season_id)


SEASONS = load_ids(GENERATOR_PATHS, MODEL_NAME, AdjacentSeriesId)


# TODO: Validate
def generate_adjacent_series(client: DivingBoard) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SEASONS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, AdjacentSeriesId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_adjacent_series(DivingBoard(build_client_automatically()))
