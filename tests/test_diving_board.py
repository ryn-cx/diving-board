"""Tests for diving_board."""

import json
from datetime import datetime, timedelta

import pytest

from diving_board import DivingBoard
from diving_board.exceptions import HTTPError

client = DivingBoard()


class TestParse:
    """Tests parsing files."""

    def test_parse_season(self) -> None:
        """Test parsing season files."""
        for json_file in client.season.json_files():
            file_content = json.loads(json_file.read_text())
            client.season.parse(file_content)

    def test_parse_playlist(self) -> None:
        """Test parsing playlist files."""
        for json_file in client.playlist.json_files():
            file_content = json.loads(json_file.read_text())
            client.playlist.parse(file_content)

    def test_parse_adjacent_series(self) -> None:
        """Test parsing adjacent series files."""
        for json_file in client.adjacent_series.json_files():
            file_content = json.loads(json_file.read_text())
            client.adjacent_series.parse(file_content)

    def test_parse_vod(self) -> None:
        """Test parsing VOD files."""
        for json_file in client.vod.json_files():
            file_content = json.loads(json_file.read_text())
            client.vod.parse(file_content)

    def test_parse_schedule(self) -> None:
        """Test parsing schedule files."""
        for json_file in client.schedule.json_files():
            file_content = json.loads(json_file.read_text())
            client.schedule.parse(file_content)


class TestExtract:
    """Tests extracting data."""

    class TestSeason:
        """Tests extracting season data."""

        def test_extract_season_hero(self) -> None:
            """Test extracting season hero."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_hero(parsed_season)

        def test_extract_season_tabs(self) -> None:
            """Test extracting season tabs."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_tabs(parsed_season)

        def test_extract_season_series(self) -> None:
            """Test extracting season series."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_series(parsed_season)

        def test_extract_season_bucket_season(self) -> None:
            """Test extracting season bucket."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_bucket_season(parsed_season)

        def test_extract_season_bucket_related(self) -> None:
            """Test extracting season related bucket."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_bucket_related(parsed_season)

        def test_extract_season_text_block(self) -> None:
            """Test extracting season text block."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_text_block(parsed_season)

    class TestPlaylist:
        """Tests extracting playlist data."""

        def test_extract_playlist_hero(self) -> None:
            """Test extracting playlist hero."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_hero(parsed_playlist)

        def test_extract_playlist_tabs(self) -> None:
            """Test extracting playlist tabs."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_tabs(parsed_playlist)

        def test_extract_playlist_bucket_playlist(self) -> None:
            """Test extracting playlist bucket."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_bucket_playlist(parsed_playlist)

        def test_extract_playlist_bucket_related(self) -> None:
            """Test extracting playlist related bucket."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_bucket_related(parsed_playlist)

        def test_extract_playlist_text_block(self) -> None:
            """Test extracting playlist text block."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_text_block(parsed_playlist)

    class TestVod:
        """Tests extracting VOD data."""

        def test_extract_vod_hero(self) -> None:
            """Test extracting VOD hero."""
            for json_file in client.vod.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_vod = client.vod.parse(json_content)
                client.vod.extract_hero(parsed_vod)

        def test_extract_vod_tabs(self) -> None:
            """Test extracting VOD tabs."""
            for json_file in client.vod.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_vod = client.vod.parse(json_content)
                client.vod.extract_tabs(parsed_vod)

        def test_extract_vod_bucket(self) -> None:
            """Test extracting VOD bucket."""
            for json_file in client.vod.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_vod = client.vod.parse(json_content)
                client.vod.extract_bucket(parsed_vod)

        def test_extract_vod_text_block(self) -> None:
            """Test extracting VOD text block."""
            for json_file in client.vod.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_vod = client.vod.parse(json_content)
                client.vod.extract_text_block(parsed_vod)

    class TestSchedule:
        """Tests extracting schedule data."""

        def test_extract_schedule_grid_block(self) -> None:
            """Test extracting schedule grid block."""
            for json_file in client.schedule.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_schedule = client.schedule.parse(json_content)
                client.schedule.extract_grid_block(parsed_schedule)

        def test_extract_schedule_filter_list(self) -> None:
            """Test extracting schedule filter list."""
            for json_file in client.schedule.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_schedule = client.schedule.parse(json_content)
                client.schedule.extract_filter_list(parsed_schedule)

        def test_extract_schedule_group_list(self) -> None:
            """Test extracting schedule group list."""
            for json_file in client.schedule.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_schedule = client.schedule.parse(json_content)
                client.schedule.extract_group_list(parsed_schedule)


class TestGet:
    """Tests getting data."""

    class TestValid:
        """Tests getting data with valid inputs."""

        def test_get_season(self) -> None:
            """Test getting a season."""
            client.season.get(19334)

        def test_get_playlist(self) -> None:
            """Test getting a playlist."""
            client.playlist.get(20431)

        def test_get_adjacent_series(self) -> None:
            """Test getting adjacent series."""
            client.adjacent_series.get(1081, 19334)

        def test_get_schedule(self) -> None:
            """Test getting the schedule."""
            client.schedule.get()

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

        def test_get_vod(self) -> None:
            """Test getting a VOD."""
            client.vod.get(532182)

    class TestInvalid:
        """Tests getting data with invalid inputs."""

        def test_get_season_invalid_id(self) -> None:
            """Test getting an invalid season."""
            with pytest.raises(HTTPError):
                client.season.get(0)

        def test_get_playlist_invalid_id(self) -> None:
            """Test getting an invalid playlist."""
            with pytest.raises(HTTPError):
                client.playlist.get(0)

        def test_get_adjacent_series_invalid_id(self) -> None:
            """Test getting an invalid adjacent series."""
            with pytest.raises(HTTPError):
                client.adjacent_series.get(0, 0)

        def test_get_vod_invalid_id(self) -> None:
            """Test getting an invalid VOD."""
            with pytest.raises(HTTPError):
                client.vod.get(0)
