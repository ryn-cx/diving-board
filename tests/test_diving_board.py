import json
from collections.abc import Iterator
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from diving_board import DivingBoard
from diving_board.constants import FILES_PATH

client = DivingBoard()


class BaseTest:
    def get_test_files(self, endpoint: str) -> Iterator[Path]:
        """Get all JSON test files for a given endpoint."""
        dir_path = FILES_PATH / endpoint
        if not dir_path.exists():
            pytest.fail(f"{dir_path} not found")

        files = dir_path.glob("*.json")

        # Make sure at least 1 file is found
        if not files:
            pytest.fail(f"No test files found in {dir_path}")

        return files


class TestParse:
    class TestSeason(BaseTest):
        def test_parse_season(self) -> None:
            """Test parsing season JSON files."""
            for json_file in self.get_test_files("season"):
                file_content = json.loads(json_file.read_text())
                client.parse_season(file_content)

        def test_extract_season_bucket_related(self) -> None:
            """Test parsing adjacent seasons JSON files."""
            for json_file in self.get_test_files("season"):
                file_content = json.loads(json_file.read_text())
                parsed = client.parse_season(file_content)
                client.extract_season_bucket_related(parsed)

        def test_extract_season_bucket_season(self) -> None:
            """Test parsing adjacent seasons JSON files."""
            for json_file in self.get_test_files("season"):
                file_content = json.loads(json_file.read_text())
                parsed = client.parse_season(file_content)
                client.extract_season_bucket_season(parsed)

        def test_extract_season_series(self) -> None:
            """Test parsing adjacent seasons JSON files."""
            for json_file in self.get_test_files("season"):
                file_content = json.loads(json_file.read_text())
                parsed = client.parse_season(file_content)
                client.extract_season_series(parsed)

    class TestAdjacentSeries(BaseTest):
        def test_parse_adjacent_series(self) -> None:
            """Test parsing adjacent seasons JSON files."""
            for json_file in self.get_test_files("adjacent_series"):
                file_content = json.loads(json_file.read_text())
                client.parse_adjacent_series(file_content)

    class TestVods(BaseTest):
        def test_parse_vod(self) -> None:
            """Test extracting hero from VOD JSON files."""
            for json_file in self.get_test_files("vod"):
                file_content = json.loads(json_file.read_text())
                client.parse_vod(file_content)

        def test_extract_vod_hero(self) -> None:
            """Test extracting hero from VOD JSON files."""
            for json_file in self.get_test_files("vod"):
                file_content = json.loads(json_file.read_text())
                parsed = client.parse_vod(file_content)
                assert client.extract_vod_hero(parsed)

        def test_extract_vod_bucket(self) -> None:
            """Test extracting bucket from VOD JSON files."""
            for json_file in self.get_test_files("vod"):
                file_content = json.loads(json_file.read_text())
                parsed = client.parse_vod(file_content)
                assert client.extract_vod_bucket(parsed)

        def test_extract_vod_tabs(self) -> None:
            """Test extracting tabs from VOD JSON files."""
            for json_file in self.get_test_files("vod"):
                file_content = json.loads(json_file.read_text())
                parsed = client.parse_vod(file_content)
                assert client.extract_vod_tabs(parsed)

        def test_extract_vod_text_block(self) -> None:
            """Test extracting text block from VOD JSON files."""
            for json_file in self.get_test_files("vod"):
                file_content = json.loads(json_file.read_text())
                parsed = client.parse_vod(file_content)
                assert client.extract_vod_text_block(parsed)

    class TestSchedule(BaseTest):
        def test_parse_schedule(self) -> None:
            """Test parsing schedule JSON files."""
            for json_file in self.get_test_files("schedule"):
                file_content = json.loads(json_file.read_text())
                client.parse_schedule(file_content)

        def test_extract_schedule_group_list(self) -> None:
            """Test parsing adjacent seasons JSON files."""
            for json_file in self.get_test_files("schedule"):
                file_content = json.loads(json_file.read_text())
                parsed = client.parse_schedule(file_content)
                client.extract_schedule_group_list(parsed)


class TestGet:
    def test_get_season(self) -> None:
        """Test getting a season."""
        client.get_season(19334)

    def test_get_adjacent_series(self) -> None:
        """Test getting other seasons for a show."""
        client.get_adjacent_series(1081, 19334)

    def test_get_schedule(self) -> None:
        """Test getting the schedule."""
        client.get_schedule()

    def test_get_schedule_until_datetime(self) -> None:
        """Test getting schedule until a specific datetime."""
        end_datetime = datetime.now().astimezone() + timedelta(days=30)
        asd = client.get_schedule_until_datetime(end_datetime=end_datetime)
        assert len(asd) > 1

    def test_get_vod(self) -> None:
        """Test getting a season."""
        client.get_vod(532182)
