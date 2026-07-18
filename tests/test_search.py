# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.search import Search


class SearchCase(BaseModel):
    query: str
    card_id: str


SEARCHES: list[SearchCase] = [
    # Series: https://www.hidive.com/series/2311
    SearchCase(query="2.5 Dimensional Seduction", card_id="SERIES#2311"),
    # Movie: https://www.hidive.com/video/796187?showInterstitial=true
    SearchCase(query="Appleseed", card_id="VOD#796187"),
]

INVALID_QUERY = "qwertyuiopasdfghjklzxcvbnm"


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Search:
    return client.search


class TestSearch:
    @pytest.mark.parametrize("case", SEARCHES)
    def test_download(self, endpoint: Search, case: SearchCase) -> None:
        download_and_save(
            endpoint,
            case.query,
            lambda: endpoint.download(case.query),
        )

    @pytest.mark.parametrize("case", SEARCHES)
    def test_parse(self, endpoint: Search, case: SearchCase) -> None:
        data = parse_json(endpoint, case.query)
        assert data.elements[0].attributes.value == case.query

    @pytest.mark.parametrize("case", SEARCHES)
    def test_extract_search(self, endpoint: Search, case: SearchCase) -> None:
        data = parse_json(endpoint, case.query)
        assert endpoint.extract_search(data).attributes.value == case.query

    @pytest.mark.parametrize("case", SEARCHES)
    def test_extract_card_list(self, endpoint: Search, case: SearchCase) -> None:
        data = parse_json(endpoint, case.query)
        card_list = endpoint.extract_card_list(data)
        assert card_list.attributes.query == case.query
        assert card_list.attributes.cards[0].attributes.action.data.id == case.card_id

    def test_invalid_download(self, endpoint: Search) -> None:
        download_and_save(
            endpoint,
            INVALID_QUERY,
            lambda: endpoint.download(INVALID_QUERY),
        )

    def test_invalid_parse(self, endpoint: Search) -> None:
        data = parse_json(endpoint, INVALID_QUERY)
        card_list = endpoint.extract_card_list(data)
        assert card_list.attributes.query == INVALID_QUERY
        assert not card_list.attributes.cards


@pytest.mark.parametrize("timezone", [None, "America/New_York"])
def test_log_id(endpoint: Search, timezone: str | None) -> None:
    query = SEARCHES[0].query
    expected = f"Search query={query!r}"
    if timezone is not None:
        expected += f" timezone={timezone!r}"
    assert endpoint.get_log_id(query, timezone) == expected
