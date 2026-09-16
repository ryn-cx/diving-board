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

MODEL_NAME = "VodModel"


# TODO: Validate
class VodId(RecordingId[DivingBoard]):
    vod_id: int

    # TODO: Validate
    def download(self, client: DivingBoard) -> str:
        return client.vod.download(self.vod_id)


VOD_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, VodId)


# TODO: Validate
def generate_vod(client: DivingBoard) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, VOD_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, VodId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_vod(DivingBoard(build_client_automatically()))
