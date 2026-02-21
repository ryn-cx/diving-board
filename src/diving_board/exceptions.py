"""Exceptions."""


class DivingBoardError(Exception):
    """Base exception for diving-board library."""


class HTTPError(DivingBoardError):
    """Raised when HTTP request fails with unexpected status code."""
