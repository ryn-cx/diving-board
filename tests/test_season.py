# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import SeasonNotFoundError
from diving_board.season.models import SeasonModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from diving_board import DivingBoard

SEASON_IDS = [
    pytest.param(24579, id="2.5 dimensional seduction season 1"),
]


class SeasonTest(RecordedEndpoint):
    MODEL = SeasonModel


# TODO: Validate
@pytest.mark.parametrize("season_id", SEASON_IDS)
def test_download(client: DivingBoard, season_id: int) -> None:
    SeasonTest.download_test(season_id, lambda: client.season.download(season_id))


# TODO: Validate
@pytest.mark.parametrize("season_id", SEASON_IDS)
def test_parse(client: DivingBoard, season_id: int) -> None:
    data = client.season.load(SeasonTest.recorded_content(season_id))
    assert data.metadata.current_season.season_id == season_id


# TODO: Validate
@pytest.mark.parametrize(
    "season_id",
    [pytest.param(0, id="season that does not exist")],
)
def test_download_invalid(client: DivingBoard, season_id: int) -> None:
    SeasonTest.error_test(
        season_id,
        lambda: client.season.download(season_id),
        SeasonNotFoundError,
    )
