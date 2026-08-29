# TODO: Validate
"""Rebuilds AdjacentSeriesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from diving_board import DivingBoard
from generate.constants import DIVING_BOARD_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

SEASONS = load_ids("AdjacentSeriesModel")
"""The series and season each recording holds the neighbouring seasons of."""


# TODO: Validate
def generate_adjacent_series(client: DivingBoard) -> None:
    """Rebuild AdjacentSeriesModel."""
    for series_id, season_id in SEASONS:
        download_if_missing(
            FILES_PATH,
            "AdjacentSeriesModel",
            f"{series_id}_{season_id}",
            lambda series_id=series_id, season_id=season_id: (
                client.adjacent_series.download(series_id, season_id)
            ),
        )
    rebuild_model(
        FILES_PATH,
        DIVING_BOARD_PATH,
        "AdjacentSeriesModel",
        name_of=lambda season: f"{season[0]}_{season[1]}",
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_adjacent_series(DivingBoard(build_client_automatically()))
