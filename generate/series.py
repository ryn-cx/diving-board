# TODO: Validate
"""Rebuilds SeriesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from diving_board import DivingBoard
from generate.constants import DIVING_BOARD_PATH, FILES_PATH
from generate.utils import download_if_missing

SERIES_IDS = [1019, 2311]


# TODO: Validate
def generate_series(client: DivingBoard) -> None:
    """Rebuild SeriesModel."""
    for series_id in SERIES_IDS:
        download_if_missing(
            FILES_PATH,
            "SeriesModel",
            series_id,
            lambda series_id=series_id: client.series.download(series_id),
        )
    generate_model(FILES_PATH, DIVING_BOARD_PATH, "SeriesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_series(DivingBoard(build_client_automatically()))
