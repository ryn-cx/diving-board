# TODO: Validate
"""Contains BaseExtractor and BaseEndpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from diving_board.constants import FILES_DIRECTORY

if TYPE_CHECKING:
    from diving_board import DivingBoard


class BaseExtractor[T: GAPIBaseModel](GAPIClient[T]):
    """Base class to extract data from API responses."""

    JSON_FILES_ROOT = FILES_DIRECTORY


class BaseEndpoint[T: GAPIBaseModel](BaseExtractor[T]):
    """Base class for API endpoints."""

    def __init__(self, client: DivingBoard) -> None:
        """Initialize the endpoint."""
        self._client = client

    def _extract_element[U: GAPIBaseModel](
        self,
        elements: list[Any],
        field_type: str,
        extractor_class: type[BaseExtractor[U]],
        *,
        update_model: bool = True,
    ) -> U:
        matches = [element for element in elements if element.field_type == field_type]
        return self._parse_single_match(
            matches,
            field_type,
            extractor_class,
            update_model=update_model,
        )

    def _extract_typed_element[U: GAPIBaseModel](
        self,
        elements: list[Any],
        field_type: str,
        attribute_type: str,
        extractor_class: type[BaseExtractor[U]],
        *,
        update_model: bool = True,
    ) -> U:
        matches = [
            element
            for element in elements
            if element.field_type == field_type
            and element.attributes.type == attribute_type
        ]
        return self._parse_single_match(
            matches,
            f"{attribute_type!r} {field_type}",
            extractor_class,
            update_model=update_model,
        )

    def _parse_single_match[U: GAPIBaseModel](
        self,
        matches: list[Any],
        type_desc: str,
        extractor_class: type[BaseExtractor[U]],
        *,
        update_model: bool = True,
    ) -> U:
        if not matches:
            msg = f"No {type_desc} element found"
            raise ValueError(msg)
        if len(matches) > 1:
            msg = f"Too many {type_desc} elements found"
            raise ValueError(msg)

        dumped = self.original_input(matches[0])
        return extractor_class().parse(dumped, update_model=update_model)
