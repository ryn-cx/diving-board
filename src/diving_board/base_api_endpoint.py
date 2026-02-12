"""Base API endpoint module."""

from __future__ import annotations

from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, Any, override

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

    @cached_property
    def json_files_folder(self) -> Path:
        """Wrapper for tests."""
        return self._json_files_folder

    @cached_property
    @override
    def _json_files_folder(self) -> Path:
        original_path = super()._json_files_folder
        # Replace underscores with folders
        subfolder = original_path.name.replace("_model", "").split("_")
        return original_path.parent.joinpath(*subfolder)


class BaseEndpoint[T: BaseModel](BaseExtractor[T]):
    """Base class for API endpoints."""

    def __init__(self, client: DivingBoard) -> None:
        """Initialize the endpoint with the DivingBoard client."""
        self._client = client

    def _extract_element[U: BaseModel](
        self,
        elements: list[Any],
        field_type: str,
        extractor_cls: type[BaseExtractor[U]],
        *,
        attribute_type: str | None = None,
        update: bool = True,
    ) -> U:
        """Extract a single element of the given type from an elements list.

        Args:
            elements: List of elements to search through.
            field_type: The ``$type`` value to match on each element.
            extractor_cls: The extractor class used to parse the element.
            attribute_type: If set, also match ``attributes.type``.
            update: Whether to update DivingBoard's models if parsing fails.

        Returns:
            The parsed element model.

        Raises:
            ValueError: If zero or more than one matching element is found.
        """
        matched: list[U] = []
        for element in elements:
            if element.field_type != field_type:
                continue
            if attribute_type is not None and element.attributes.type != attribute_type:
                continue
            dumped = self._dump_response(element)
            parsed = extractor_cls().parse(dumped, update=update)
            matched.append(parsed)

        type_desc = field_type
        if attribute_type is not None:
            type_desc = f"{attribute_type!r} {field_type}"

        if len(matched) == 0:
            msg = f"No {type_desc} element found"
            raise ValueError(msg)

        if len(matched) > 1:
            msg = f"Too many {type_desc} elements found: {len(matched)}"
            raise ValueError(msg)

        return matched[0]
