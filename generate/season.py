# TODO: Validate
"""Rebuilds SeasonModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from diving_board import DivingBoard
from generate.constants import DIVING_BOARD_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

SEASON_IDS = load_ids("SeasonModel")


# TODO: Validate
def generate_season(client: DivingBoard) -> None:
    """Rebuild SeasonModel."""
    for season_id in SEASON_IDS:
        download_if_missing(
            FILES_PATH,
            "SeasonModel",
            season_id,
            lambda season_id=season_id: client.season.download(season_id),
        )
    rebuild_model(FILES_PATH, DIVING_BOARD_PATH, "SeasonModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season(DivingBoard(build_client_automatically()))
