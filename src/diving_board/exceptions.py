# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class DivingBoardError(Exception):
    """Base exception for DivingBoard."""

    response: str | dict[str, Any] | None = None


# TODO: Validate
class HTTPError(DivingBoardError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


# TODO: Validate
class VodNotFoundError(ResourceNotFoundError):
    """Raised when the requested video does not exist."""

    # TODO: Validate
    def __init__(
        self,
        vod_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the video id and the originating response."""
        self.vod_id = vod_id
        super().__init__(status_code, response)


# TODO: Validate
class SeriesNotFoundError(ResourceNotFoundError):
    """Raised when the requested series does not exist."""

    # TODO: Validate
    def __init__(
        self,
        series_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the series id and the originating response."""
        self.series_id = series_id
        super().__init__(status_code, response)


# TODO: Validate
class SeasonNotFoundError(ResourceNotFoundError):
    """Raised when the requested season does not exist."""

    # TODO: Validate
    def __init__(
        self,
        season_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the season id and the originating response."""
        self.season_id = season_id
        super().__init__(status_code, response)


# TODO: Validate
class AdjacentSeriesNotFoundError(ResourceNotFoundError):
    """Raised when the season is not one of the series' seasons."""

    # TODO: Validate
    def __init__(
        self,
        series_id: int,
        season_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the series id, season id and originating response."""
        self.series_id = series_id
        self.season_id = season_id
        super().__init__(status_code, response)
