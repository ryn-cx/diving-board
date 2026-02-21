"""Base API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, override

from good_ass_pydantic_integrator import CustomSerializer, GAPIClient
from pydantic import BaseModel

from diving_board.constants import FILES_PATH

if TYPE_CHECKING:
    from pathlib import Path

    from diving_board import DivingBoard


class BaseExtractor[T: BaseModel](GAPIClient[T]):
    """Base class to extract data from API responses."""

    @staticmethod
    def _naive_datetime_serializer(
        class_name: str,
        field_name: str,
    ) -> CustomSerializer:
        """Create a CustomSerializer for a NaiveDatetime field.

        Args:
            class_name: The Pydantic model class name containing the field.
            field_name: The field name to serialize.

        Returns:
            A CustomSerializer that formats NaiveDatetime as ``%Y-%m-%dT%H:%M``.
        """
        return CustomSerializer(
            class_name=class_name,
            field_name=field_name,
            serializer_code='return value.strftime("%Y-%m-%dT%H:%M")',
            input_type="NaiveDatetime",
            output_type="str",
        )

    @override
    @classmethod
    def json_files_folder(cls) -> Path:
        folder_name = cls._to_folder_name(cls._get_model_name())
        original_path = FILES_PATH / folder_name
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
        update_model: bool = True,
    ) -> U:
        """Extract a single element of the given type from an elements list.

        Args:
            elements: List of elements to search through.
            field_type: The ``$type`` value to match on each element.
            extractor_cls: The extractor class used to parse the element.
            attribute_type: If set, also match ``attributes.type``.
            update_model: Whether to update DivingBoard's models if parsing fails.

        Returns:
            The parsed element model.

        Raises:
            ValueError: If zero or more than one matching element is found.
        """
        type_desc = field_type
        if attribute_type is not None:
            type_desc = f"{attribute_type!r} {field_type}"

        result: U | None = None
        for element in elements:
            if element.field_type != field_type:
                continue
            if attribute_type and element.attributes.type != attribute_type:
                continue
            if result:
                msg = f"Too many {type_desc} elements found"
                raise ValueError(msg)
            dumped = self.dump_response(element)
            result = extractor_cls().parse(dumped, update_model=update_model)

        if result is None:
            msg = f"No {type_desc} element found"
            raise ValueError(msg)

        return result
