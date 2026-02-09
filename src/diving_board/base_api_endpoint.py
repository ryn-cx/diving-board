"""Base API endpoint module."""

from __future__ import annotations

from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, override

from gapi import GAPIClient
from pydantic import BaseModel

from diving_board.constants import FILES_PATH

if TYPE_CHECKING:
    from pathlib import Path

    from diving_board import DivingBoard


class BaseExtractor[T: BaseModel](GAPIClient[T]):
    """Base class to extract data from API responses."""

    @cached_property
    @override
    def _root_files_path(self) -> Path:
        return FILES_PATH


class BaseEndpoint[T: BaseModel](BaseExtractor[T]):
    """Base class for API endpoints."""

    def __init__(self, client: DivingBoard) -> None:
        """Initialize the endpoint with the DivingBoard client."""
        self._client = client
