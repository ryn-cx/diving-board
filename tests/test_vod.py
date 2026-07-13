from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_http_error, data_path, download_if_missing

if TYPE_CHECKING:
    from pathlib import Path

    from diving_board import DivingBoard
    from diving_board.vod import Vod
    from diving_board.vod.models import VodModel

VIDEO_ID = 655773


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Vod:
    return client.vod


@pytest.fixture(scope="session")
def json_file(endpoint: Vod) -> Path:
    return data_path(endpoint, str(VIDEO_ID))


@pytest.fixture(scope="session")
def data(endpoint: Vod, json_file: Path) -> VodModel:
    return endpoint.parse(json.loads(json_file.read_text()))


class TestVod:
    def test_download(self, endpoint: Vod) -> None:
        download_if_missing(
            endpoint,
            str(VIDEO_ID),
            lambda: endpoint.download(VIDEO_ID),
        )

    def test_value(self, data: VodModel) -> None:
        assert any(element.attributes.id == VIDEO_ID for element in data.elements)

    def test_extract_hero(self, endpoint: Vod, data: VodModel) -> None:
        assert any(
            item.attributes.id == VIDEO_ID
            for item in endpoint.extract_hero(data).attributes.content
        )

    def test_extract_tabs(self, endpoint: Vod, data: VodModel) -> None:
        assert endpoint.extract_tabs(data).attributes.id == VIDEO_ID

    def test_extract_bucket(self, endpoint: Vod, data: VodModel) -> None:
        assert endpoint.extract_bucket(data).attributes.type == "related"

    def test_extract_text_block(self, endpoint: Vod, data: VodModel) -> None:
        assert endpoint.extract_text_block(data).attributes.text == "Related content"

    def test_invalid(self, endpoint: Vod) -> None:
        assert_http_error(endpoint, "0", lambda: endpoint.download(0))
