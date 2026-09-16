# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import SeasonNotFoundError

if TYPE_CHECKING:
    from diving_board import DivingBoard

SEASON_IDS = [pytest.param(24579, id="2.5 dimensional seduction season 1")]


# TODO: Validate
@pytest.mark.parametrize("season_id", SEASON_IDS)
def test_download(client: DivingBoard, season_id: int) -> None:
    season = client.season(season_id)
    assert season.metadata.current_season.season_id == season_id


# TODO: Validate
def test_download_invalid(client: DivingBoard) -> None:
    with pytest.raises(SeasonNotFoundError):
        client.season.download(0)
