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

MODEL_NAME = "SeasonModel"


# TODO: Validate
class SeasonId(RecordingId[DivingBoard]):
    season_id: int

    # TODO: Validate
    def download(self, client: DivingBoard) -> str:
        return client.season.download(self.season_id)


SEASON_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, SeasonId)


# TODO: Validate
def generate_season(client: DivingBoard) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SEASON_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, SeasonId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season(DivingBoard(build_client_automatically()))
