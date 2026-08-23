# TODO: Validate
"""Rebuilds VodModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from diving_board import DivingBoard
from generate.constants import DIVING_BOARD_PATH, FILES_PATH
from generate.utils import download_if_missing

VOD_IDS = [655773, 796187]


# TODO: Validate
def generate_vod(client: DivingBoard) -> None:
    """Rebuild VodModel."""
    for vod_id in VOD_IDS:
        download_if_missing(
            FILES_PATH,
            "VodModel",
            vod_id,
            lambda vod_id=vod_id: client.vod.download(vod_id),
        )
    generate_model(FILES_PATH, DIVING_BOARD_PATH, "VodModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_vod(DivingBoard(build_client_automatically()))
