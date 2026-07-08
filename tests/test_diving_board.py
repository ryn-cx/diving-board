# TODO: Validate
"""Tests for diving_board."""

from __future__ import annotations

import json
from datetime import datetime, timedelta

import pytest

from diving_board import DivingBoard
from diving_board.exceptions import HTTPError

client = DivingBoard()


class TestGet:
    """Test live get requests across every endpoint."""

    def test_get_season(self) -> None:
        """Test getting a season."""
        model = client.season.get(19334)
        client.season.save_new_json_file(client.season.dump(model))

    def test_get_playlist(self) -> None:
        """Test getting a playlist."""
        model = client.playlist.get(20431)
        client.playlist.save_new_json_file(client.playlist.dump(model))

    def test_get_vod(self) -> None:
        """Test getting a VOD."""
        model = client.vod.get(532182)
        client.vod.save_new_json_file(client.vod.dump(model))

    def test_get_series(self) -> None:
        """Test getting a series."""
        model = client.series.get(1286)
        client.series.save_new_json_file(client.series.dump(model))

    def test_get_adjacent_series(self) -> None:
        """Test getting adjacent series."""
        model = client.adjacent_series.get(1081, 19334)
        client.adjacent_series.save_new_json_file(client.adjacent_series.dump(model))

    def test_get_schedule(self) -> None:
        """Test getting the schedule."""
        model = client.schedule.get()
        client.schedule.save_new_json_file(client.schedule.dump(model))

    def test_get_schedule_from(self) -> None:
        """Test getting the schedule with a from_ value."""
        today = datetime.now().astimezone()
        first_of_month = today.replace(
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )
        model = client.schedule.get(from_=first_of_month)
        client.schedule.save_new_json_file(client.schedule.dump(model))

    def test_get_schedule_until_datetime(self) -> None:
        """Test getting schedule until datetime."""
        end_datetime = datetime.now().astimezone() + timedelta(days=30)
        schedules = client.schedule.get_until_datetime(end_datetime=end_datetime)
        assert len(schedules) > 1

    def test_get_schedule_past_last_seen(self) -> None:
        """Test getting schedule past last seen."""
        end_datetime = datetime.now().astimezone() + timedelta(days=365)
        schedules = client.schedule.get_until_datetime(end_datetime=end_datetime)
        assert len(schedules) > 1

    def test_get_search(self) -> None:
        """Test searching."""
        model = client.search.get("One")
        client.search.save_new_json_file(client.search.dump(model))


class TestInvalidGet:
    """Test get requests for missing or invalid resources."""

    def test_invalid_get_season(self) -> None:
        """Test getting an invalid season."""
        with pytest.raises(HTTPError):
            client.season.get(0)

    def test_invalid_get_playlist(self) -> None:
        """Test getting an invalid playlist."""
        with pytest.raises(HTTPError):
            client.playlist.get(0)

    def test_invalid_get_vod(self) -> None:
        """Test getting an invalid VOD."""
        with pytest.raises(HTTPError):
            client.vod.get(0)

    def test_invalid_get_series(self) -> None:
        """Test getting an invalid series."""
        with pytest.raises(HTTPError):
            client.series.get(0)

    def test_invalid_get_adjacent_series(self) -> None:
        """Test getting an invalid adjacent series."""
        with pytest.raises(HTTPError):
            client.adjacent_series.get(0, 0)


class TestParse:
    """Test parsing every saved file for each endpoint."""

    def test_parse_season(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.season.json_files():
            client.season.parse(json.loads(json_file.read_text()))

    def test_parse_playlist(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.playlist.json_files():
            client.playlist.parse(json.loads(json_file.read_text()))

    def test_parse_vod(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.vod.json_files():
            client.vod.parse(json.loads(json_file.read_text()))

    def test_parse_series(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.series.json_files():
            client.series.parse(json.loads(json_file.read_text()))

    def test_parse_adjacent_series(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.adjacent_series.json_files():
            client.adjacent_series.parse(json.loads(json_file.read_text()))

    def test_parse_schedule(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.schedule.json_files():
            client.schedule.parse(json.loads(json_file.read_text()))

    def test_parse_search(self) -> None:
        """Test parsing every saved file."""
        for json_file in client.search.json_files():
            client.search.parse(json.loads(json_file.read_text()))


class TestExtract:
    """Test extracting typed entries from saved responses."""

    def test_extract_season_hero(self) -> None:
        """Test extracting season hero."""
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_hero(model)

    def test_extract_season_tabs(self) -> None:
        """Test extracting season tabs."""
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_tabs(model)

    def test_extract_season_series(self) -> None:
        """Test extracting season series."""
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_series(model)

    def test_extract_season_bucket_season(self) -> None:
        """Test extracting season bucket."""
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_bucket_season(model)

    def test_extract_season_bucket_related(self) -> None:
        """Test extracting season related bucket."""
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_bucket_related(model)

    def test_extract_season_text_block(self) -> None:
        """Test extracting season text block."""
        for json_file in client.season.json_files():
            model = client.season.parse(json.loads(json_file.read_text()))
            client.season.extract_text_block(model)

    def test_extract_playlist_hero(self) -> None:
        """Test extracting playlist hero."""
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_hero(model)

    def test_extract_playlist_tabs(self) -> None:
        """Test extracting playlist tabs."""
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_tabs(model)

    def test_extract_playlist_bucket_playlist(self) -> None:
        """Test extracting playlist bucket."""
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_bucket_playlist(model)

    def test_extract_playlist_bucket_related(self) -> None:
        """Test extracting playlist related bucket."""
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_bucket_related(model)

    def test_extract_playlist_text_block(self) -> None:
        """Test extracting playlist text block."""
        for json_file in client.playlist.json_files():
            model = client.playlist.parse(json.loads(json_file.read_text()))
            client.playlist.extract_text_block(model)

    def test_extract_vod_hero(self) -> None:
        """Test extracting VOD hero."""
        for json_file in client.vod.json_files():
            model = client.vod.parse(json.loads(json_file.read_text()))
            client.vod.extract_hero(model)

    def test_extract_vod_tabs(self) -> None:
        """Test extracting VOD tabs."""
        for json_file in client.vod.json_files():
            model = client.vod.parse(json.loads(json_file.read_text()))
            client.vod.extract_tabs(model)

    def test_extract_vod_bucket(self) -> None:
        """Test extracting VOD bucket."""
        for json_file in client.vod.json_files():
            model = client.vod.parse(json.loads(json_file.read_text()))
            client.vod.extract_bucket(model)

    def test_extract_vod_text_block(self) -> None:
        """Test extracting VOD text block."""
        for json_file in client.vod.json_files():
            model = client.vod.parse(json.loads(json_file.read_text()))
            client.vod.extract_text_block(model)

    def test_extract_schedule_grid_block(self) -> None:
        """Test extracting schedule grid block."""
        for json_file in client.schedule.json_files():
            model = client.schedule.parse(json.loads(json_file.read_text()))
            client.schedule.extract_grid_block(model)

    def test_extract_schedule_filter_list(self) -> None:
        """Test extracting schedule filter list."""
        for json_file in client.schedule.json_files():
            model = client.schedule.parse(json.loads(json_file.read_text()))
            client.schedule.extract_filter_list(model)

    def test_extract_schedule_group_list(self) -> None:
        """Test extracting schedule group list."""
        for json_file in client.schedule.json_files():
            model = client.schedule.parse(json.loads(json_file.read_text()))
            client.schedule.extract_group_list(model)

    def test_extract_search_input(self) -> None:
        """Test extracting search input."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_input(model)

    def test_extract_search_filter_list(self) -> None:
        """Test extracting search filter list."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_filter_list(model)

    def test_extract_search_sort_list(self) -> None:
        """Test extracting search sort list."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_sort_list(model)

    def test_extract_search_card_list(self) -> None:
        """Test extracting search card list."""
        for json_file in client.search.json_files():
            model = client.search.parse(json.loads(json_file.read_text()))
            client.search.extract_card_list(model)
