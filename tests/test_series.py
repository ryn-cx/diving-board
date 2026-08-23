# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import SeriesNotFoundError
from diving_board.series.models import SeriesModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from diving_board import DivingBoard

SERIES_IDS = [
    pytest.param(2311, id="2.5 dimensional seduction - one season"),
    pytest.param(1019, id="ahiru no sora - four seasons"),
]


class SeriesTest(RecordedEndpoint):
    MODEL = SeriesModel


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: DivingBoard, series_id: int) -> None:
    SeriesTest.download_test(series_id, lambda: client.series.download(series_id))


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_parse(client: DivingBoard, series_id: int) -> None:
    data = client.series.load(SeriesTest.recorded_content(series_id))
    assert data.metadata.series.series_id == series_id


# TODO: Validate
@pytest.mark.parametrize(
    "series_id",
    [pytest.param(0, id="series that does not exist")],
)
def test_download_invalid(client: DivingBoard, series_id: int) -> None:
    SeriesTest.error_test(
        series_id,
        lambda: client.series.download(series_id),
        SeriesNotFoundError,
    )
