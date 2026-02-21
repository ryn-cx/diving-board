"""Tests for diving_board."""

import json
from datetime import datetime, timedelta

import pytest

from diving_board import DivingBoard
from diving_board.exceptions import HTTPError

client = DivingBoard()


class TestParsing:
    """Tests for parsing API responses."""

    class TestSeason:
        """Tests for season parsing."""

        def test_parse_season(self) -> None:
            """Test parsing season JSON files."""
            for json_file in client.season.json_files():
                file_content = json.loads(json_file.read_text())
                client.season.parse(file_content)

        def test_extract_season_hero(self) -> None:
            """Test extracting hero from season JSON files."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_hero(parsed_season)

        def test_extract_season_tabs(self) -> None:
            """Test extracting tabs from season JSON files."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_tabs(parsed_season)

        def test_extract_season_series(self) -> None:
            """Test extracting series from season JSON files."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_series(parsed_season)

        def test_extract_season_bucket_season(self) -> None:
            """Test extracting season bucket from season JSON files."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_bucket_season(parsed_season)

        def test_extract_season_bucket_related(self) -> None:
            """Test extracting related bucket from season JSON files."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_bucket_related(parsed_season)

        def test_extract_season_text_block(self) -> None:
            """Test extracting text block from season JSON files."""
            for json_file in client.season.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_season = client.season.parse(json_content)
                client.season.extract_text_block(parsed_season)

    class TestPlaylist:
        """Tests for playlist parsing."""

        def test_parse_playlist(self) -> None:
            """Test parsing playlist JSON files."""
            for json_file in client.playlist.json_files():
                file_content = json.loads(json_file.read_text())
                client.playlist.parse(file_content)

        def test_extract_playlist_hero(self) -> None:
            """Test extracting hero from playlist JSON files."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_hero(parsed_playlist)

        def test_extract_playlist_tabs(self) -> None:
            """Test extracting tabs from playlist JSON files."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_tabs(parsed_playlist)

        def test_extract_playlist_bucket_playlist(self) -> None:
            """Test extracting playlist bucket from playlist JSON files."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_bucket_playlist(parsed_playlist)

        def test_extract_playlist_bucket_related(self) -> None:
            """Test extracting related bucket from playlist JSON files."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_bucket_related(parsed_playlist)

        def test_extract_playlist_text_block(self) -> None:
            """Test extracting text block from playlist JSON files."""
            for json_file in client.playlist.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_playlist = client.playlist.parse(json_content)
                client.playlist.extract_text_block(parsed_playlist)

    class TestAdjacentSeries:
        """Tests for adjacent series parsing."""

        def test_parse_adjacent_series(self) -> None:
            """Test parsing adjacent seasons JSON files."""
            for json_file in client.adjacent_series.json_files():
                file_content = json.loads(json_file.read_text())
                client.adjacent_series.parse(file_content)

    class TestVods:
        """Tests for VOD parsing."""

        def test_parse_vod(self) -> None:
            """Test parsing VOD JSON files."""
            for json_file in client.vod.json_files():
                file_content = json.loads(json_file.read_text())
                client.vod.parse(file_content)

        def test_extract_vod_hero(self) -> None:
            """Test extracting hero from VOD JSON files."""
            for json_file in client.vod.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_vod = client.vod.parse(json_content)
                client.vod.extract_hero(parsed_vod)

        def test_extract_vod_tabs(self) -> None:
            """Test extracting tabs from VOD JSON files."""
            for json_file in client.vod.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_vod = client.vod.parse(json_content)
                client.vod.extract_tabs(parsed_vod)

        def test_extract_vod_bucket(self) -> None:
            """Test extracting bucket from VOD JSON files."""
            for json_file in client.vod.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_vod = client.vod.parse(json_content)
                client.vod.extract_bucket(parsed_vod)

        def test_extract_vod_text_block(self) -> None:
            """Test extracting text block from VOD JSON files."""
            for json_file in client.vod.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_vod = client.vod.parse(json_content)
                client.vod.extract_text_block(parsed_vod)

    class TestSchedule:
        """Tests for schedule parsing."""

        def test_parse_schedule(self) -> None:
            """Test parsing schedule JSON files."""
            for json_file in client.schedule.json_files():
                file_content = json.loads(json_file.read_text())
                client.schedule.parse(file_content)

        def test_extract_schedule_grid_block(self) -> None:
            """Test extracting grid block from schedule JSON files."""
            for json_file in client.schedule.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_schedule = client.schedule.parse(json_content)
                client.schedule.extract_grid_block(parsed_schedule)

        def test_extract_schedule_filter_list(self) -> None:
            """Test extracting filter list from schedule JSON files."""
            for json_file in client.schedule.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_schedule = client.schedule.parse(json_content)
                client.schedule.extract_filter_list(parsed_schedule)

        def test_extract_schedule_group_list(self) -> None:
            """Test extracting group list from schedule JSON files."""
            for json_file in client.schedule.json_files():
                json_content = json.loads(json_file.read_text())
                parsed_schedule = client.schedule.parse(json_content)
                client.schedule.extract_group_list(parsed_schedule)


class TestGet:
    """Tests for downloading and parsing API responses.

    These tests intentionally do not mock downloads because the goal of these tests is
    to detect changes in the API.
    """

    class TestValid:
        """Tests for downloading valid resources."""

        def test_get_season(self) -> None:
            """Test getting a season."""
            client.season.get(19334)

        def test_get_playlist(self) -> None:
            """Test getting a playlist."""
            client.playlist.get(20431)

        def test_get_adjacent_series(self) -> None:
            """Test getting other seasons for a show."""
            client.adjacent_series.get(1081, 19334)

        def test_get_schedule(self) -> None:
            """Test getting the schedule."""
            client.schedule.get()

        def test_get_schedule_until_datetime(self) -> None:
            """Test getting schedule until a specific datetime."""
            end_datetime = datetime.now().astimezone() + timedelta(days=30)
            schedules = client.schedule.get_until_datetime(end_datetime=end_datetime)
            assert len(schedules) > 1

        def test_get_schedule_past_last_seen(self) -> None:
            """Test getting schedule past the last seen pagination token."""
            end_datetime = datetime.now().astimezone() + timedelta(days=365)
            schedules = client.schedule.get_until_datetime(end_datetime=end_datetime)
            assert len(schedules) > 1

        def test_get_vod(self) -> None:
            """Test getting a VOD."""
            client.vod.get(532182)

    class TestInvalid:
        """Tests for downloading resources with invalid IDs."""

        def test_get_season_invalid_id(self) -> None:
            """Test getting a season with an invalid ID."""
            with pytest.raises(HTTPError):
                client.season.get(0)

        def test_get_playlist_invalid_id(self) -> None:
            """Test getting a playlist with an invalid ID."""
            with pytest.raises(HTTPError):
                client.playlist.get(0)

        def test_get_adjacent_series_invalid_id(self) -> None:
            """Test getting adjacent series with an invalid ID."""
            with pytest.raises(HTTPError):
                client.adjacent_series.get(0, 0)

        def test_get_vod_invalid_id(self) -> None:
            """Test getting a VOD with an invalid ID."""
            with pytest.raises(HTTPError):
                client.vod.get(0)
