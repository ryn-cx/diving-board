# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import AdjacentSeriesNotFoundError

if TYPE_CHECKING:
    from diving_board import DivingBoard

SEASONS = [
    pytest.param(1019, 18908, id="ahiru no sora - first season"),
    pytest.param(1019, 18909, id="ahiru no sora - middle season"),
    pytest.param(1019, 18911, id="ahiru no sora - last season"),
    pytest.param(2311, 24579, id="2.5 dimensional seduction - only season"),
]


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_id"), SEASONS)
def test_download(client: DivingBoard, series_id: int, season_id: int) -> None:
    adjacent = client.adjacent_series(series_id, season_id)
    seasons = (adjacent.preceding_seasons or []) + (adjacent.following_seasons or [])
    # The season that was asked about is not one of the seasons either side of it.
    assert season_id not in [season.id for season in seasons]


# TODO: Validate
def test_download_invalid(client: DivingBoard) -> None:
    with pytest.raises(AdjacentSeriesNotFoundError):
        # A season that is not the series' own.
        client.adjacent_series.download(2311, 18908)
