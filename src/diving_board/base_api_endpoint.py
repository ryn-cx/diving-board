# TODO: Validate
from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, override

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from diving_board.constants import FILES_PATH
from diving_board.exceptions import NoContentError

if TYPE_CHECKING:
    from pathlib import Path

    from diving_board import DivingBoard


class BaseExtractor[T: GAPIBaseModel](GAPIClient[T]):
    """Base class to extract data from API responses."""

    @override
    @classmethod
    def json_files_folder(cls) -> Path:
        folder_name = cls._folder_name(cls._model_name())
        original_path = FILES_PATH / folder_name
        subfolder = original_path.name.replace("_model", "").split("_")
        return original_path.parent.joinpath(*subfolder)


class BaseEndpoint[T: GAPIBaseModel](BaseExtractor[T]):
    """Base class for API endpoints."""

    def __init__(self, client: DivingBoard) -> None:
        """Initialize the endpoint with the DivingBoard client."""
        self._client = client

    @staticmethod
    @abstractmethod
    def has_content(*args: Any, **kwargs: Any) -> bool:  # noqa: ANN401
        """Return whether the response has meaningful content."""

    def _parse_or_raise(self, response: dict[str, Any], *, has_content: bool) -> T:
        """Parse `response`, or raise `NoContentError` when it is empty.

        This is the single place `get` decides "nothing here". The raised
        `NoContentError` carries `response`, so callers can still recover the
        downloaded payload from the exception.

        Args:
            response: The raw JSON response to parse.
            has_content: The endpoint's `has_content` verdict for `response`.

        Returns:
            The parsed model.

        Raises:
            NoContentError: If `has_content` is false.
        """
        if not has_content:
            raise NoContentError(response, endpoint=type(self).__name__)
        return self.parse(response)

    def _extract_element[U: GAPIBaseModel](
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
            dumped = self.original_input(element)
            result = extractor_cls().parse(dumped, update_model=update_model)

        if result is None:
            msg = f"No {type_desc} element found"
            raise ValueError(msg)

        return result
