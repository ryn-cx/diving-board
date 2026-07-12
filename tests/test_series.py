from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import HTTPError

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.series import Series


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Series:
    return client.series


class TestSeries:
    def test_get(self, endpoint: Series) -> None:
        """https://www.hidive.com/series/2311"""
        series_id = 2311
        data = endpoint.get(series_id)
        assert data.metadata.series.series_id == series_id
        endpoint.save_new_json_file(endpoint.original_input(data))

    def test_invalid_get(self, endpoint: Series) -> None:
        with pytest.raises(HTTPError):
            endpoint.get(0)

    def test_parse(self, endpoint: Series) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))
