# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import VodNotFoundError
from diving_board.vod.models import VodModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from diving_board import DivingBoard

VOD_IDS = [
    pytest.param(655773, id="2.5 dimensional seduction episode 1"),
    pytest.param(796187, id="appleseed film"),
]


class VodTest(RecordedEndpoint):
    MODEL = VodModel


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
    VodTest.download_test(vod_id, lambda: client.vod.download(vod_id))


# TODO: Validate
@pytest.mark.parametrize("vod_id", VOD_IDS)
def test_parse(client: DivingBoard, vod_id: int) -> None:
    data = client.vod.load(VodTest.recorded_content(vod_id))
    assert tabs_id(data) == vod_id


# TODO: Validate
@pytest.mark.parametrize(
    "vod_id",
    [pytest.param(0, id="video that does not exist")],
)
def test_download_invalid(client: DivingBoard, vod_id: int) -> None:
    VodTest.error_test(
        vod_id,
        lambda: client.vod.download(vod_id),
        VodNotFoundError,
    )
