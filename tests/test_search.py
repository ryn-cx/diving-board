# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.search.models import SearchModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from diving_board import DivingBoard

QUERIES = [
    pytest.param("2.5 Dimensional Seduction", id="series result"),
    pytest.param("Appleseed", id="film result"),
    pytest.param("qwertyuiopasdfghjklzxcvbnm", id="query nothing matches"),
]


class SearchTest(RecordedEndpoint):
    MODEL = SearchModel


# TODO: Validate
def searched_query(search: SearchModel) -> str | None:
    """Return the query the cards were found for, as the API echoes it back."""
    return next(
        element.attributes.query
        for element in search.elements or []
        if element.field_type == "cardList"
    )


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: DivingBoard, query: str) -> None:
    SearchTest.download_test(query, lambda: client.search.download(query))


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(client: DivingBoard, query: str) -> None:
    data = client.search.load(SearchTest.recorded_content(query))
    assert searched_query(data) == query
