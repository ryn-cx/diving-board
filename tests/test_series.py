# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import HTTPError
from tests.utils import assert_error, download_and_save, parse_json

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.series import Series

SERIES_ID = 2311
INVALID_SERIES_ID = 0


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Series:
    return client.series


class TestSeries:
    def test_download(self, endpoint: Series) -> None:
        download_and_save(
            endpoint,
            str(SERIES_ID),
            lambda: endpoint.download(SERIES_ID),
        )

    def test_parse(self, endpoint: Series) -> None:
        data = parse_json(endpoint, str(SERIES_ID))
        assert data.metadata.series.series_id == SERIES_ID

    def test_invalid_download(self, endpoint: Series) -> None:
        assert_error(
            endpoint,
            str(INVALID_SERIES_ID),
            lambda: endpoint.download(INVALID_SERIES_ID),
            HTTPError,
        )


@pytest.mark.parametrize("timezone", [None, "America/New_York"])
def test_log_id(endpoint: Series, timezone: str | None) -> None:
    expected = f"Series series_id={SERIES_ID!r}"
    if timezone is not None:
        expected += f" timezone={timezone!r}"
    assert endpoint.get_log_id(SERIES_ID, timezone) == expected
