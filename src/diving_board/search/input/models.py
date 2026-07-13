# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    placeholder: str
    placeholder_label: str = Field(..., alias="placeholderLabel")
    value: str
    action: Action


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int


class SearchInputModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
    style: Style
