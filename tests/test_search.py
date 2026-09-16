# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.search.models import SearchModel

QUERIES = [
    pytest.param("2.5 Dimensional Seduction", id="series result"),
    pytest.param("Appleseed", id="film result"),
    pytest.param("qwertyuiopasdfghjklzxcvbnm", id="query nothing matches"),
]


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
    assert searched_query(client.search(query)) == query
