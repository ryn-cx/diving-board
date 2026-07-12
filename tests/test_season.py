from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import HTTPError

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.season import Season


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Season:
    return client.season


class TestSeason:
    def test_get(self, endpoint: Season) -> None:
        """https://www.hidive.com/season/24579?seriesId=2311"""
        season_id = 24579
        name = "2.5 Dimensional Seduction"
        data = endpoint.get(season_id)

        assert data.metadata.current_season.season_id == season_id
        assert data.metadata.series.title == name
        assert endpoint.extract_hero(data).attributes.header.attributes.text == name
        assert endpoint.extract_series(data).attributes.series.title == name

        endpoint.save_new_json_file(endpoint.original_input(data))

    def test_invalid_get(self, endpoint: Season) -> None:
        with pytest.raises(HTTPError):
            endpoint.get(0)

    def test_parse(self, endpoint: Season) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_hero(self, endpoint: Season) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_hero(data)

    def test_extract_tabs(self, endpoint: Season) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_tabs(data)

    def test_extract_series(self, endpoint: Season) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_series(data)

    def test_extract_bucket_season(self, endpoint: Season) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_bucket_season(data)

    def test_extract_bucket_related(self, endpoint: Season) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_bucket_related(data)

    def test_extract_text_block(self, endpoint: Season) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_text_block(data)
