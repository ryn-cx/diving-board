# TODO: Validate
"""Rebuilds VodModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from diving_board import DivingBoard
from generate.constants import DIVING_BOARD_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

VOD_IDS = load_ids("VodModel")


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
    rebuild_model(FILES_PATH, DIVING_BOARD_PATH, "VodModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_vod(DivingBoard(build_client_automatically()))
