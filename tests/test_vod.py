# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import HTTPError
from tests.utils import assert_error, download_and_save, parse_json

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.vod import Vod

VIDEO_ID = 655773
INVALID_VIDEO_ID = 0


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Vod:
    return client.vod


class TestVod:
    def test_download(self, endpoint: Vod) -> None:
        download_and_save(
            endpoint,
            str(VIDEO_ID),
            lambda: endpoint.download(VIDEO_ID),
        )

    def test_parse(self, endpoint: Vod) -> None:
        data = parse_json(endpoint, str(VIDEO_ID))
        assert any(element.attributes.id == VIDEO_ID for element in data.elements)

    def test_extract_hero(self, endpoint: Vod) -> None:
        data = parse_json(endpoint, str(VIDEO_ID))
        assert any(
            item.attributes.id == VIDEO_ID
            for item in endpoint.extract_hero(data).attributes.content
        )

    def test_extract_tabs(self, endpoint: Vod) -> None:
        data = parse_json(endpoint, str(VIDEO_ID))
        assert endpoint.extract_tabs(data).attributes.id == VIDEO_ID

    def test_extract_bucket(self, endpoint: Vod) -> None:
        data = parse_json(endpoint, str(VIDEO_ID))
        assert endpoint.extract_bucket(data).attributes.type == "related"

    def test_extract_text_block(self, endpoint: Vod) -> None:
        data = parse_json(endpoint, str(VIDEO_ID))
        assert endpoint.extract_text_block(data).attributes.text == "Related content"

    def test_invalid_download(self, endpoint: Vod) -> None:
        assert_error(
            endpoint,
            str(INVALID_VIDEO_ID),
            lambda: endpoint.download(INVALID_VIDEO_ID),
            HTTPError,
        )


@pytest.mark.parametrize("timezone", [None, "America/New_York"])
def test_log_id(endpoint: Vod, timezone: str | None) -> None:
    expected = f"Vod vod_id={VIDEO_ID!r}"
    if timezone is not None:
        expected += f" timezone={timezone!r}"
    assert endpoint.get_log_id(VIDEO_ID, timezone) == expected
