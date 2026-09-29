# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SearchModel as OptionalModel
from .strict_models import SearchModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Action,
        Action1,
        Attributes,
        Attributes1,
        Attributes2,
        Attributes3,
        Card,
        ContentItem,
        Data,
        Data1,
        Element,
        HeaderItem,
        SearchModel,
        Style,
        Style1,
    )
else:
    from .optional_models import (
        Action,
        Action1,
        Attributes,
        Attributes1,
        Attributes2,
        Attributes3,
        Card,
        ContentItem,
        Data,
        Data1,
        Element,
        HeaderItem,
        SearchModel,
        Style,
        Style1,
    )

__all__ = [
    "Action",
    "Action1",
    "Attributes",
    "Attributes1",
    "Attributes2",
    "Attributes3",
    "Card",
    "ContentItem",
    "Data",
    "Data1",
    "Element",
    "HeaderItem",
    "SearchModel",
    "Style",
    "Style1",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SearchModel:
    """Read a downloaded file into SearchModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
