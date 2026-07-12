from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from diving_board import DivingBoard
    from diving_board.search import Search

QUERY = "2.5 Dimensional Seduction"


@pytest.fixture(scope="session")
def endpoint(client: DivingBoard) -> Search:
    return client.search


class TestSearch:
    def test_get(self, endpoint: Search) -> None:
        data = endpoint.get(QUERY)

        assert endpoint.extract_input(data).attributes.value == QUERY
        assert endpoint.extract_card_list(data).attributes.query == QUERY
        assert any(
            content.attributes.text == QUERY
            for card in endpoint.extract_card_list(data).attributes.cards
            for content in card.attributes.content
            if content.field_type == "textBlock"
        )
        assert any(
            card.attributes.action.data.title == QUERY
            for card in endpoint.extract_card_list(data).attributes.cards
        )

        endpoint.save_new_json_file(endpoint.original_input(data))

    def test_invalid_get(self, endpoint: Search) -> None:
        query = "qwertyuiopasdfghjklzxcvbnm"
        data = endpoint.get(query)

        assert any(
            element.attributes.empty_title == "noResults" for element in data.elements
        )
        assert any(element.attributes.empty_title is None for element in data.elements)

        endpoint.save_new_json_file(endpoint.original_input(data))

    def test_parse(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))

    def test_extract_input(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_input(model)

    def test_extract_filter_list(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_filter_list(model)

    def test_extract_sort_list(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_sort_list(model)

    def test_extract_card_list(self, endpoint: Search) -> None:
        for json_file in endpoint.json_files():
            model = endpoint.parse(json.loads(json_file.read_text()))
            endpoint.extract_card_list(model)
