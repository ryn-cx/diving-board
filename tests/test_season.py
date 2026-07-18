# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import HTTPError
from tests.utils import assert_error, download_and_save, parse_json

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.season import Season

SEASON_ID = 24579
INVALID_SEASON_ID = 0
NAME = "2.5 Dimensional Seduction"


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Season:
    return client.season


class TestSeason:
    def test_download(self, endpoint: Season) -> None:
        download_and_save(
            endpoint,
            str(SEASON_ID),
            lambda: endpoint.download(SEASON_ID),
        )

    def test_parse(self, endpoint: Season) -> None:
        data = parse_json(endpoint, str(SEASON_ID))
        assert data.metadata.current_season.season_id == SEASON_ID
        assert data.metadata.series.title == NAME

    def test_extract_hero(self, endpoint: Season) -> None:
        data = parse_json(endpoint, str(SEASON_ID))
        assert endpoint.extract_hero(data).attributes.header.attributes.text == NAME

    def test_extract_tabs(self, endpoint: Season) -> None:
        data = parse_json(endpoint, str(SEASON_ID))
        assert endpoint.extract_tabs(data)

    def test_extract_series(self, endpoint: Season) -> None:
        data = parse_json(endpoint, str(SEASON_ID))
        assert endpoint.extract_series(data).attributes.series.title == NAME

    def test_extract_bucket_season(self, endpoint: Season) -> None:
        data = parse_json(endpoint, str(SEASON_ID))
        assert endpoint.extract_bucket_season(data).attributes.season_id == SEASON_ID

    def test_extract_bucket_related(self, endpoint: Season) -> None:
        data = parse_json(endpoint, str(SEASON_ID))
        assert endpoint.extract_bucket_related(data).attributes.season_id == SEASON_ID

    def test_extract_text_block(self, endpoint: Season) -> None:
        data = parse_json(endpoint, str(SEASON_ID))
        assert endpoint.extract_text_block(data).attributes.text == "Related content"

    def test_invalid_download(self, endpoint: Season) -> None:
        assert_error(
            endpoint,
            str(INVALID_SEASON_ID),
            lambda: endpoint.download(INVALID_SEASON_ID),
            HTTPError,
        )


@pytest.mark.parametrize("timezone", [None, "America/New_York"])
def test_log_id(endpoint: Season, timezone: str | None) -> None:
    expected = f"Season season_id={SEASON_ID!r}"
    if timezone is not None:
        expected += f" timezone={timezone!r}"
    assert endpoint.get_log_id(SEASON_ID, timezone) == expected
