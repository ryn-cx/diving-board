# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import SeriesNotFoundError

if TYPE_CHECKING:
    from diving_board import DivingBoard

SERIES_IDS = [
    pytest.param(2311, id="2.5 dimensional seduction - one season"),
    pytest.param(1019, id="ahiru no sora - four seasons"),
]


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: DivingBoard, series_id: int) -> None:
    series = client.series(series_id)
    assert series.metadata.series.series_id == series_id


# TODO: Validate
def test_download_invalid(client: DivingBoard) -> None:
    with pytest.raises(SeriesNotFoundError):
        client.series.download(0)
