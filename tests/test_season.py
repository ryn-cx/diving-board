# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_http_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from diving_board import DivingBoard
    from diving_board.season import Season
    from diving_board.season.models import SeasonModel

SEASON_ID = 24579
NAME = "2.5 Dimensional Seduction"


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Season:
    return client.season


@pytest.fixture(scope="session")
def json_file(endpoint: Season) -> Path:
    return data_path(endpoint, str(SEASON_ID))


@pytest.fixture(scope="session")
def data(endpoint: Season, json_file: Path) -> SeasonModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSeason:
    def test_download(self, endpoint: Season) -> None:
        download_if_missing(
            endpoint,
            str(SEASON_ID),
            lambda: endpoint.download(SEASON_ID),
        )

    def test_value(self, data: SeasonModel) -> None:
        assert data.metadata.current_season.season_id == SEASON_ID
        assert data.metadata.series.title == NAME

    def test_extract_hero(self, endpoint: Season, data: SeasonModel) -> None:
        assert endpoint.extract_hero(data).attributes.header.attributes.text == NAME

    def test_extract_tabs(self, endpoint: Season, data: SeasonModel) -> None:
        assert endpoint.extract_tabs(data)

    def test_extract_series(self, endpoint: Season, data: SeasonModel) -> None:
        assert endpoint.extract_series(data).attributes.series.title == NAME

    def test_extract_bucket_season(self, endpoint: Season, data: SeasonModel) -> None:
        assert endpoint.extract_bucket_season(data).attributes.season_id == SEASON_ID

    def test_extract_bucket_related(self, endpoint: Season, data: SeasonModel) -> None:
        assert endpoint.extract_bucket_related(data).attributes.season_id == SEASON_ID

    def test_extract_text_block(self, endpoint: Season, data: SeasonModel) -> None:
        assert endpoint.extract_text_block(data).attributes.text == "Related content"

    def test_invalid(self, endpoint: Season) -> None:
        assert_http_error(endpoint, "0", lambda: endpoint.download(0))
