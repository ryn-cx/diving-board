"""SeasonModel, strict to a type checker, all-optional at runtime.

A type checker reads the strict model, so every field carries the type and
the requiredness the schema recorded. At runtime the all-optional copy is imported
instead, so a response that has drifted still parses and a field the data is
missing is None despite what its type hint says.
"""

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SeasonModel as OptionalModel
from .strict_models import SeasonModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Action,
        Action1,
        Action2,
        Action3,
        Attributes,
        Attributes1,
        Attributes2,
        Attributes3,
        Attributes4,
        Attributes5,
        Attributes6,
        Attributes7,
        Button,
        ContentDownload,
        ContentItem,
        CurrentSeason,
        CurrentVod,
        Data,
        Data1,
        Data2,
        Desktop,
        Element,
        GroupName,
        Header,
        Image,
        Item,
        Item1,
        Metadata,
        Mobile,
        Paging,
        Paging1,
        SeasonModel,
        Seasons,
        Series,
        Style,
        Tablet,
        Tag,
        Token,
        Tv,
    )
else:
    from .optional_models import (
        Action,
        Action1,
        Action2,
        Action3,
        Attributes,
        Attributes1,
        Attributes2,
        Attributes3,
        Attributes4,
        Attributes5,
        Attributes6,
        Attributes7,
        Button,
        ContentDownload,
        ContentItem,
        CurrentSeason,
        CurrentVod,
        Data,
        Data1,
        Data2,
        Desktop,
        Element,
        GroupName,
        Header,
        Image,
        Item,
        Item1,
        Metadata,
        Mobile,
        Paging,
        Paging1,
        SeasonModel,
        Seasons,
        Series,
        Style,
        Tablet,
        Tag,
        Token,
        Tv,
    )

__all__ = [
    "Action",
    "Action1",
    "Action2",
    "Action3",
    "Attributes",
    "Attributes1",
    "Attributes2",
    "Attributes3",
    "Attributes4",
    "Attributes5",
    "Attributes6",
    "Attributes7",
    "Button",
    "ContentDownload",
    "ContentItem",
    "CurrentSeason",
    "CurrentVod",
    "Data",
    "Data1",
    "Data2",
    "Desktop",
    "Element",
    "GroupName",
    "Header",
    "Image",
    "Item",
    "Item1",
    "Metadata",
    "Mobile",
    "Paging",
    "Paging1",
    "SeasonModel",
    "Seasons",
    "Series",
    "Style",
    "Tablet",
    "Tag",
    "Token",
    "Tv",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SeasonModel:
    """Read a downloaded file into SeasonModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
