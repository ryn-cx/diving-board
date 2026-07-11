# TODO: Validate
from __future__ import annotations

import json
from datetime import datetime, timedelta

import pytest
from get_around import build_client_automatically

from diving_board import DivingBoard
from diving_board.exceptions import HTTPError, NoContentError

client = DivingBoard(build_client_automatically())

SEASON_ID = 19334
"""season_id of Hidamari Sketch Season 3."""
PLAYLIST_ID = 20431
"""playlist_id of a playlist."""
VOD_ID = 532182
"""vod_id of a VOD."""
SERIES_ID = 1286
"""series_id of Tamako Market."""
ADJACENT_SERIES_ID = 1081
"""series_id of Hidamari Sketch, used for adjacent series lookups."""
SEARCH_QUERY = "One"
"""A search term used for the search endpoint."""
INVALID_ID = 0
"""An id that does not correspond to any resource."""
INVALID_SEARCH_QUERY = "qwertyuiopasdfghjklzxcvbnm"
"""A search query that matches nothing."""


class TestGet:
    def test_get_season(self) -> None:
        endpoint = client.season
        model = endpoint.get(SEASON_ID)
        assert model.metadata.current_season.season_id == SEASON_ID
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_playlist(self) -> None:
        endpoint = client.playlist
        model = endpoint.get(PLAYLIST_ID)
        assert any(element.attributes.id == PLAYLIST_ID for element in model.elements)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_vod(self) -> None:
        endpoint = client.vod
        model = endpoint.get(VOD_ID)
        assert any(element.attributes.id == VOD_ID for element in model.elements)
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_series(self) -> None:
        endpoint = client.series
        model = endpoint.get(SERIES_ID)
        assert model.metadata.series.series_id == SERIES_ID
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_adjacent_series(self) -> None:
        endpoint = client.adjacent_series
        model = endpoint.get(ADJACENT_SERIES_ID, SEASON_ID)
        # The queried series_id/season_id identify the reference point and are not
        # echoed in the body; the response lists the seasons adjacent to it.
        assert model.following_seasons
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_schedule(self) -> None:
        endpoint = client.schedule
        model = endpoint.get()
        assert model.elements
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_schedule_from(self) -> None:
        endpoint = client.schedule
        first_of_month = (
            datetime.now()
            .astimezone()
            .replace(
                day=1,
                hour=0,
                minute=0,
                second=0,
                microsecond=0,
            )
        )
        model = endpoint.get(from_=first_of_month)
        assert model.elements
        endpoint.save_new_json_file(endpoint.original_input(model))

    def test_get_schedule_until_datetime(self) -> None:
        end_datetime = datetime.now().astimezone() + timedelta(days=30)
        schedules = client.schedule.get_until_datetime(end_datetime=end_datetime)
        assert len(schedules) > 1

    def test_get_schedule_past_last_seen(self) -> None:
        end_datetime = datetime.now().astimezone() + timedelta(days=365)
        schedules = client.schedule.get_until_datetime(end_datetime=end_datetime)
        assert len(schedules) > 1

    def test_get_search(self) -> None:
        endpoint = client.search
        model = endpoint.get(SEARCH_QUERY)
        assert any(
            element.attributes.query == SEARCH_QUERY for element in model.elements
        )
        endpoint.save_new_json_file(endpoint.original_input(model))


class TestInvalidGet:
    def test_invalid_get_season(self) -> None:
        with pytest.raises(HTTPError):
            client.season.get(INVALID_ID)

    def test_invalid_get_playlist(self) -> None:
        with pytest.raises(HTTPError):
            client.playlist.get(INVALID_ID)

    def test_invalid_get_vod(self) -> None:
        with pytest.raises(HTTPError):
            client.vod.get(INVALID_ID)

    def test_invalid_get_series(self) -> None:
        with pytest.raises(HTTPError):
            client.series.get(INVALID_ID)

    def test_invalid_get_adjacent_series(self) -> None:
        with pytest.raises(HTTPError):
            client.adjacent_series.get(INVALID_ID, INVALID_ID)

    def test_invalid_get_schedule(self) -> None:
        pytest.skip("The schedule endpoint takes no id and cannot be made invalid.")

    def test_invalid_get_search(self) -> None:
        # An unmatched search query returns a 200 with the search scaffolding but
        # no cards, which surfaces as NoContentError.
        with pytest.raises(NoContentError) as error:
            client.search.get(INVALID_SEARCH_QUERY)
        # The payload is still recoverable from the raised exception.
        assert "elements" in error.value.response


class TestParse:
    @pytest.mark.parametrize(
        "endpoint_name",
        [
            "season",
            "playlist",
            "vod",
            "series",
            "adjacent_series",
            "schedule",
            "search",
        ],
    )
    def test_parse(self, endpoint_name: str) -> None:
        endpoint = getattr(client, endpoint_name)
        for json_file in endpoint.json_files():
            endpoint.parse(json.loads(json_file.read_text()))


class TestExtract:
    def test_extract_season_hero(self) -> None:
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_hero(model)

    def test_extract_season_tabs(self) -> None:
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_tabs(model)

    def test_extract_season_series(self) -> None:
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_series(model)

    def test_extract_season_bucket_season(self) -> None:
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_bucket_season(model)

    def test_extract_season_bucket_related(self) -> None:
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_bucket_related(model)

    def test_extract_season_text_block(self) -> None:
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_text_block(model)

    def test_extract_playlist_hero(self) -> None:
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_hero(model)

    def test_extract_playlist_tabs(self) -> None:
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_tabs(model)

    def test_extract_playlist_bucket_playlist(self) -> None:
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_bucket_playlist(model)

    def test_extract_playlist_bucket_related(self) -> None:
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_bucket_related(model)

    def test_extract_playlist_text_block(self) -> None:
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_text_block(model)

    def test_extract_vod_hero(self) -> None:
        for json_file in client.vod.json_files():
            model = client.vod.parse(json.loads(json_file.read_text()))
            client.vod.extract_hero(model)

    def test_extract_vod_tabs(self) -> None:
        for json_file in client.vod.json_files():
            model = client.vod.parse(json.loads(json_file.read_text()))
            client.vod.extract_tabs(model)

    def test_extract_vod_bucket(self) -> None:
        for json_file in client.vod.json_files():
            model = client.vod.parse(json.loads(json_file.read_text()))
            client.vod.extract_bucket(model)

    def test_extract_vod_text_block(self) -> None:
        for json_file in client.vod.json_files():
            model = client.vod.parse(json.loads(json_file.read_text()))
            client.vod.extract_text_block(model)

    def test_extract_schedule_grid_block(self) -> None:
        for json_file in client.schedule.json_files():
            model = client.schedule.parse(json.loads(json_file.read_text()))
            client.schedule.extract_grid_block(model)

    def test_extract_schedule_filter_list(self) -> None:
        for json_file in client.schedule.json_files():
            model = client.schedule.parse(json.loads(json_file.read_text()))
            client.schedule.extract_filter_list(model)

    def test_extract_schedule_group_list(self) -> None:
        for json_file in client.schedule.json_files():
            model = client.schedule.parse(json.loads(json_file.read_text()))
            client.schedule.extract_group_list(model)

    def test_extract_search_input(self) -> None:
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_input(model)

    def test_extract_search_filter_list(self) -> None:
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_filter_list(model)

    def test_extract_search_sort_list(self) -> None:
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_sort_list(model)

    def test_extract_search_card_list(self) -> None:
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_card_list(model)
