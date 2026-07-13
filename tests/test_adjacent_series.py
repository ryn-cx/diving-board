# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from tests.utils import assert_http_error, data_path, download_if_missing

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.adjacent_series import SeriesAdjacentTo


class TestData(BaseModel):
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


SERIES_AND_SEASONS: list[TestData] = [
    # Series with multiple seasons. Tests on season 2 and 3 overlap, but both are tested
    # for completeness.
    # https://www.hidive.com/series/1019
    TestData(
        series_id=MULTIPLE_SEASON_SERIES_ID,
        season_id=FIRST_SEASON_ID,
        preceding_ids=[],
        following_ids=[SECOND_SEASON_ID, THIRD_SEASON_ID, FOURTH_SEASON_ID],
    ),
    TestData(
        series_id=MULTIPLE_SEASON_SERIES_ID,
        season_id=SECOND_SEASON_ID,
        preceding_ids=[FIRST_SEASON_ID],
        following_ids=[THIRD_SEASON_ID, FOURTH_SEASON_ID],
    ),
    TestData(
        series_id=MULTIPLE_SEASON_SERIES_ID,
        season_id=THIRD_SEASON_ID,
        preceding_ids=[FIRST_SEASON_ID, SECOND_SEASON_ID],
        following_ids=[FOURTH_SEASON_ID],
    ),
    TestData(
        series_id=MULTIPLE_SEASON_SERIES_ID,
        season_id=FOURTH_SEASON_ID,
        preceding_ids=[FIRST_SEASON_ID, SECOND_SEASON_ID, THIRD_SEASON_ID],
        following_ids=[],
    ),
    # Series with a single season
    # https://www.hidive.com/season/24579?seriesId=2311
    TestData(
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
    @pytest.mark.parametrize("test_data", SERIES_AND_SEASONS)
    def test_download(self, endpoint: SeriesAdjacentTo, test_data: TestData) -> None:
        name = f"{test_data.series_id}_{test_data.season_id}"
        download_if_missing(
            endpoint,
            name,
            lambda: endpoint.download(test_data.series_id, test_data.season_id),
        )

    @pytest.mark.parametrize("test_data", SERIES_AND_SEASONS)
    def test_valid(self, endpoint: SeriesAdjacentTo, test_data: TestData) -> None:
        name = f"{test_data.series_id}_{test_data.season_id}"
        data = endpoint.parse(json.loads(data_path(endpoint, name).read_text()))
        assert [
            season.id for season in data.preceding_seasons
        ] == test_data.preceding_ids
        assert [
            season.id for season in data.following_seasons
        ] == test_data.following_ids

    def test_invalid(self, endpoint: SeriesAdjacentTo) -> None:
        name = f"{SINGLE_SEASON_SERIES_ID}_{FIRST_SEASON_ID}"
        assert_http_error(
            endpoint,
            name,
            lambda: endpoint.download(SINGLE_SEASON_SERIES_ID, FIRST_SEASON_ID),
        )
