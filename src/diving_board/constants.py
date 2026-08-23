# TODO: Validate
"""Constants."""

from collections.abc import Mapping, Sequence
from pathlib import Path

DIVING_BOARD_PATH = Path(__file__).parent
FILES_PATH = DIVING_BOARD_PATH / "_files"

BASE_API_URL = "https://dce-frontoffice.imggaming.com"
"""Where the site's own front office API lives, which every view is read from."""

type JSON_VALUE = (
    str | int | float | bool | Mapping[str, JSON_VALUE] | Sequence[JSON_VALUE] | None
)
"""Anything that can appear in a parsed JSON document."""
