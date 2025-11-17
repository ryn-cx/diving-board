import json
from collections.abc import Iterator
from pathlib import Path

import pytest

from diving_board import DivingBoard
from diving_board.constants import FILES_PATH

client = DivingBoard()


class TestParsing:
    def get_test_files(self, endpoint: str) -> Iterator[Path]:
        """Get all JSON test files for a given endpoint."""
        dir_path = FILES_PATH / endpoint
        if not dir_path.exists():
            pytest.fail(f"{dir_path} not found")

        files = dir_path.glob("*.json")

        # Make sure at least 1 file is found
        if not any(files):
            pytest.fail(f"No test files found in {dir_path}")

        return files

    def test_parse_season(self) -> None:
        """Test parsing season JSON files."""
        for json_file in self.get_test_files("season"):
            file_content = json.loads(json_file.read_text())
            parsed = client.parse_season(file_content)
            dumped = parsed.model_dump(mode="json", by_alias=True, exclude_unset=True)
            assert file_content == dumped

    def test_parse_other_seasons(self) -> None:
        """Test parsing other seasons JSON files."""
        for json_file in self.get_test_files("other_seasons"):
            file_content = json.loads(json_file.read_text())
            parsed = client.parse_other_seasons(file_content)
            assert file_content == client.dump_response(parsed)


class TestGet:
    def test_get_season(self) -> None:
        """Test getting a season."""
        client.get_season(18914)

    def test_get_other_seasons(self) -> None:
        """Test getting other seasons for a show."""
        client.get_other_seasons(1081, 19337)
