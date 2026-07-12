from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import HTTPError

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.adjacent_series import SeriesAdjacentTo


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> SeriesAdjacentTo:
    return client.adjacent_series_to


class TestAdjacentSeries:
    def test_single_season(self, endpoint: SeriesAdjacentTo) -> None:
        """https://www.hidive.com/season/24579?seriesId=2311"""
        data = endpoint.get(2311, 24579)
        assert not data.preceding_seasons
        assert not data.following_seasons
        endpoint.save_new_json_file(endpoint.original_input(data))

    def test_middle_season(self, endpoint: SeriesAdjacentTo) -> None:
        """https://www.hidive.com/season/18909?seriesId=1019"""
        previous_season_id = 18908
        next_season_id = 18910
        data = endpoint.get(1019, 18909)

        assert data.preceding_seasons
        assert data.following_seasons
        # Seasons are ordered ascending, so the directly adjacent seasons are the
        # closest preceding (last) and closest following (first) entries.
        assert data.preceding_seasons[-1].id == previous_season_id
        assert data.following_seasons[0].id == next_season_id

        endpoint.save_new_json_file(endpoint.original_input(data))

    def test_mismatched_series_and_season(self, endpoint: SeriesAdjacentTo) -> None:
        with pytest.raises(HTTPError):
            endpoint.get(2311, 18908)

    def test_parse(self, endpoint: SeriesAdjacentTo) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
