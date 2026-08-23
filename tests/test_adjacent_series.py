# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.adjacent_series.models import AdjacentSeriesModel
from diving_board.exceptions import AdjacentSeriesNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from diving_board import DivingBoard

SEASONS = [
    pytest.param(1019, 18908, id="ahiru no sora - first season"),
    pytest.param(1019, 18909, id="ahiru no sora - middle season"),
    pytest.param(1019, 18911, id="ahiru no sora - last season"),
    pytest.param(2311, 24579, id="2.5 dimensional seduction - only season"),
]


class AdjacentSeriesTest(RecordedEndpoint):
    MODEL = AdjacentSeriesModel


# TODO: Validate
def recording_name(series_id: int, season_id: int) -> str:
    """Return the name the seasons either side of one season are recorded under."""
    return f"{series_id}_{season_id}"


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_id"), SEASONS)
def test_download(client: DivingBoard, series_id: int, season_id: int) -> None:
    AdjacentSeriesTest.download_test(
        recording_name(series_id, season_id),
        lambda: client.adjacent_series.download(series_id, season_id),
    )


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_id"), SEASONS)
def test_parse(client: DivingBoard, series_id: int, season_id: int) -> None:
    data = client.adjacent_series.load(
        AdjacentSeriesTest.recorded_content(recording_name(series_id, season_id)),
    )
    seasons = (data.preceding_seasons or []) + (data.following_seasons or [])
    # The season that was asked about is not one of the seasons either side of it.
    assert season_id not in [season.id for season in seasons]


# TODO: Validate
@pytest.mark.parametrize(
    ("series_id", "season_id"),
    [pytest.param(2311, 18908, id="season that is not the series' own")],
)
def test_download_invalid(client: DivingBoard, series_id: int, season_id: int) -> None:
    AdjacentSeriesTest.error_test(
        recording_name(series_id, season_id),
        lambda: client.adjacent_series.download(series_id, season_id),
        AdjacentSeriesNotFoundError,
    )
