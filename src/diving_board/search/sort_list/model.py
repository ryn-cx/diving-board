# ruff: noqa: D100, D101
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str


class Title(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style


class Option(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    field: str
    direction: str
    is_active: bool = Field(..., alias="isActive")


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    action: Action
    title: Title
    options: list[Option]


class SearchSortListModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
