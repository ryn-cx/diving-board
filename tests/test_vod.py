# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import VodNotFoundError

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.vod.models import VodModel

VOD_IDS = [
    pytest.param(655773, id="2.5 dimensional seduction episode 1"),
    pytest.param(796187, id="appleseed film"),
]


# TODO: Validate
def tabs_id(vod: VodModel) -> int | None:
    """Return the id of the video the file is for."""
    return next(
        element.attributes.id
        for element in vod.elements or []
        if element.field_type == "tabs"
    )


# TODO: Validate
@pytest.mark.parametrize("vod_id", VOD_IDS)
def test_download(client: DivingBoard, vod_id: int) -> None:
    assert tabs_id(client.vod(vod_id)) == vod_id


# TODO: Validate
def test_download_invalid(client: DivingBoard) -> None:
    with pytest.raises(VodNotFoundError):
        client.vod.download(0)
