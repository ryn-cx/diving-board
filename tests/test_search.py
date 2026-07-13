# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from tests.utils import data_path, download_if_missing

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.search import Search


class TestData(BaseModel):
    query: str
    card_id: str


SEARCHES: list[TestData] = [
    # Series: https://www.hidive.com/series/2311
    TestData(query="2.5 Dimensional Seduction", card_id="SERIES#2311"),
    # Movie: https://www.hidive.com/video/796187?showInterstitial=true
    TestData(query="Appleseed", card_id="VOD#796187"),
]

INVALID_QUERY = "qwertyuiopasdfghjklzxcvbnm"


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Search:
    return client.search


class TestSearch:
    @pytest.mark.parametrize("test_data", SEARCHES)
    def test_download(self, endpoint: Search, test_data: TestData) -> None:
        download_if_missing(
            endpoint,
            test_data.query,
            lambda: endpoint.download(test_data.query),
        )

    @pytest.mark.parametrize("test_data", SEARCHES)
    def test_valid(self, endpoint: Search, test_data: TestData) -> None:
        data = endpoint.parse(
            json.loads(data_path(endpoint, test_data.query).read_text()),
        )
        assert data.elements[0].attributes.value == test_data.query

    @pytest.mark.parametrize("test_data", SEARCHES)
    def test_extract_search(self, endpoint: Search, test_data: TestData) -> None:
        data = endpoint.parse(
            json.loads(data_path(endpoint, test_data.query).read_text()),
        )
        assert endpoint.extract_search(data).attributes.value == test_data.query

    @pytest.mark.parametrize("test_data", SEARCHES)
    def test_extract_card_list(self, endpoint: Search, test_data: TestData) -> None:
        data = endpoint.parse(
            json.loads(data_path(endpoint, test_data.query).read_text()),
        )
        card_list = endpoint.extract_card_list(data)
        assert card_list.attributes.query == test_data.query
        assert (
            card_list.attributes.cards[0].attributes.action.data.id == test_data.card_id
        )

    def test_invalid(self, endpoint: Search) -> None:
        download_if_missing(
            endpoint,
            INVALID_QUERY,
            lambda: endpoint.download(INVALID_QUERY),
        )
        data = endpoint.parse(
            json.loads(data_path(endpoint, INVALID_QUERY).read_text()),
        )
        card_list = endpoint.extract_card_list(data)
        assert card_list.attributes.query == INVALID_QUERY
        assert not card_list.attributes.cards
