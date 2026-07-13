# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_http_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from diving_board import DivingBoard
    from diving_board.series import Series
    from diving_board.series.models import SeriesModel

SERIES_ID = 2311


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Series:
    return client.series


@pytest.fixture(scope="session")
def json_file(endpoint: Series) -> Path:
    return data_path(endpoint, str(SERIES_ID))


@pytest.fixture(scope="session")
def data(endpoint: Series, json_file: Path) -> SeriesModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestSeries:
    def test_download(self, endpoint: Series) -> None:
        download_if_missing(
            endpoint,
            str(SERIES_ID),
            lambda: endpoint.download(SERIES_ID),
        )

    def test_value(self, data: SeriesModel) -> None:
        assert data.metadata.series.series_id == SERIES_ID

    def test_invalid(self, endpoint: Series) -> None:
        assert_http_error(endpoint, "0", lambda: endpoint.download(0))
