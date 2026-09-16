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

MODEL_NAME = "SeriesModel"


# TODO: Validate
class SeriesId(RecordingId[DivingBoard]):
    series_id: int

    # TODO: Validate
    def download(self, client: DivingBoard) -> str:
        return client.series.download(self.series_id)


SERIES_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, SeriesId)


# TODO: Validate
def generate_series(client: DivingBoard) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SERIES_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, SeriesId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_series(DivingBoard(build_client_automatically()))
