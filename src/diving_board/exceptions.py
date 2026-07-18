# TODO: Validate
"""Exceptions."""

from __future__ import annotations


class DivingBoardError(Exception):
    """Base exception for DivingBoard."""


class HTTPError(DivingBoardError):
    """Raised when HTTP request fails with unexpected status code."""
