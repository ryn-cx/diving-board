# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from diving_board.exceptions import HTTPError
from tests.utils import assert_error, download_and_save, parse_json

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.adjacent_series import SeriesAdjacentTo


class AdjacentCase(BaseModel):
    series_id: int
    season_id: int
    preceding_ids: list[int]
    following_ids: list[int]


MULTIPLE_SEASON_SERIES_ID = 1019
FIRST_SEASON_ID = 18908
SECOND_SEASON_ID = 18909
THIRD_SEASON_ID = 18910
FOURTH_SEASON_ID = 18911

SINGLE_SEASON_SERIES_ID = 2311
SINGLE_SEASON_ID = 24579


SERIES_AND_SEASONS: list[AdjacentCase] = [
    # Series with multiple seasons. Tests on season 2 and 3 overlap, but both are tested
    # for completeness.
    # https://www.hidive.com/series/1019
    AdjacentCase(
        series_id=MULTIPLE_SEASON_SERIES_ID,
        season_id=FIRST_SEASON_ID,
        preceding_ids=[],
        following_ids=[SECOND_SEASON_ID, THIRD_SEASON_ID, FOURTH_SEASON_ID],
    ),
    AdjacentCase(
        series_id=MULTIPLE_SEASON_SERIES_ID,
        season_id=SECOND_SEASON_ID,
        preceding_ids=[FIRST_SEASON_ID],
        following_ids=[THIRD_SEASON_ID, FOURTH_SEASON_ID],
    ),
    AdjacentCase(
        series_id=MULTIPLE_SEASON_SERIES_ID,
        season_id=THIRD_SEASON_ID,
        preceding_ids=[FIRST_SEASON_ID, SECOND_SEASON_ID],
        following_ids=[FOURTH_SEASON_ID],
    ),
    AdjacentCase(
        series_id=MULTIPLE_SEASON_SERIES_ID,
        season_id=FOURTH_SEASON_ID,
        preceding_ids=[FIRST_SEASON_ID, SECOND_SEASON_ID, THIRD_SEASON_ID],
        following_ids=[],
    ),
    # Series with a single season
    # https://www.hidive.com/season/24579?seriesId=2311
    AdjacentCase(
        series_id=SINGLE_SEASON_SERIES_ID,
        season_id=SINGLE_SEASON_ID,
        preceding_ids=[],
        following_ids=[],
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> SeriesAdjacentTo:
    return client.adjacent_series_to


class TestAdjacentSeries:
    @pytest.mark.parametrize("case", SERIES_AND_SEASONS)
    def test_download(self, endpoint: SeriesAdjacentTo, case: AdjacentCase) -> None:
        name = f"{case.series_id}_{case.season_id}"
        download_and_save(
            endpoint,
            name,
            lambda: endpoint.download(case.series_id, case.season_id),
        )

    @pytest.mark.parametrize("case", SERIES_AND_SEASONS)
    def test_parse(self, endpoint: SeriesAdjacentTo, case: AdjacentCase) -> None:
        name = f"{case.series_id}_{case.season_id}"
        data = parse_json(endpoint, name)
        assert [season.id for season in data.preceding_seasons] == case.preceding_ids
        assert [season.id for season in data.following_seasons] == case.following_ids

    def test_invalid_download(self, endpoint: SeriesAdjacentTo) -> None:
        name = f"{SINGLE_SEASON_SERIES_ID}_{FIRST_SEASON_ID}"
        assert_error(
            endpoint,
            name,
            lambda: endpoint.download(SINGLE_SEASON_SERIES_ID, FIRST_SEASON_ID),
            HTTPError,
        )


def test_log_id(endpoint: SeriesAdjacentTo) -> None:
    expected = (
        f"SeriesAdjacentTo series_id={MULTIPLE_SEASON_SERIES_ID!r} "
        f"season_id={FIRST_SEASON_ID!r}"
    )
    assert (
        endpoint.get_log_id(MULTIPLE_SEASON_SERIES_ID, FIRST_SEASON_ID) == expected
    )
