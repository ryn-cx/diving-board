# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.content_grid import (
    MOVIES_GRID_VIEW_CONFIG_ID,
    RESULTS_PER_PAGE,
    SERIES_GRID_VIEW_CONFIG_ID,
)

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.content_grid.models import ContentGridModel

GRIDS = [
    pytest.param(SERIES_GRID_VIEW_CONFIG_ID, id="series"),
    pytest.param(MOVIES_GRID_VIEW_CONFIG_ID, id="movies"),
]


# TODO: Validate
def cards(content_grid: ContentGridModel) -> int:
    """Return how many cards the page carries."""
    listed = next(
        element.attributes.cards
        for element in content_grid.elements or []
        if element.field_type == "cardList"
    )
    return len(listed or [])


# TODO: Validate
@pytest.mark.parametrize("grid_view_config_id", GRIDS)
def test_download(client: DivingBoard, grid_view_config_id: str) -> None:
    assert cards(client.content_grid(grid_view_config_id)) == RESULTS_PER_PAGE


# TODO: Validate
def test_download_next_page(client: DivingBoard) -> None:
    # The site pages the grid by the token the page before it handed back.
    first_page = client.content_grid.download(SERIES_GRID_VIEW_CONFIG_ID)
    last_seen = client.content_grid.next_page_token(first_page)
    next_page = client.content_grid(SERIES_GRID_VIEW_CONFIG_ID, last_seen=last_seen)
    assert cards(next_page) == RESULTS_PER_PAGE


# TODO: Validate
def test_download_all(client: DivingBoard) -> None:
    pages = client.content_grid.download_all(MOVIES_GRID_VIEW_CONFIG_ID)
    # Every page but the last one is full, and the last one is where the walk
    # stops because it has no token to go on with.
    assert client.content_grid.next_page_token(pages[-1]) is None
    full_pages = client.content_grid.load_pages(pages[:-1])
    assert all(cards(page) == RESULTS_PER_PAGE for page in full_pages)
    assert 0 < cards(client.content_grid.load(pages[-1])) <= RESULTS_PER_PAGE
