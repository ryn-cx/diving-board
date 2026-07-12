from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from diving_board.exceptions import HTTPError

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.vod import Vod


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Vod:
    return client.vod


class TestVod:
    def test_get(self, endpoint: Vod) -> None:
        """https://www.hidive.com/video/655773?showInterstitial=true"""
        video_id = 655773
        data = endpoint.get(video_id)

        assert any(element.attributes.id == video_id for element in data.elements)
        assert any(
            item.attributes.id == video_id
            for item in endpoint.extract_hero(data).attributes.content
        )
        assert endpoint.extract_tabs(data).attributes.id == video_id
        endpoint.save_new_json_file(endpoint.original_input(data))

    def test_invalid_get(self, endpoint: Vod) -> None:
        with pytest.raises(HTTPError):
            endpoint.get(0)

    def test_parse(self, endpoint: Vod) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_hero(self, endpoint: Vod) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_hero(data)

    def test_extract_tabs(self, endpoint: Vod) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_tabs(data)

    def test_extract_bucket(self, endpoint: Vod) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_bucket(data)

    def test_extract_text_block(self, endpoint: Vod) -> None:
        for json_file in endpoint.json_files():
            data = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_text_block(data)
