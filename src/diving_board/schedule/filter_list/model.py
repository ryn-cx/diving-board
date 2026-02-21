# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int
    color: str


class Title(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style


class Attributes3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    number_of_lines: int = Field(..., alias="numberOfLines")


class Style1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str


class Title1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3
    style: Style1


class Option(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    filter_key: str = Field(..., alias="filterKey")
    is_active: bool = Field(..., alias="isActive")
    text: str
    format: str
    value: str


class Attributes2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title1
    filter_key: str = Field(..., alias="filterKey")
    options: list[Option]


class Filter(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Reset(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    text: str
    action: Action


class Action1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Apply(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    text: str
    action: Action1


class Actions(BaseModel):
    model_config = ConfigDict(extra="forbid")
    reset: Reset
    apply: Apply


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title
    filters: list[Filter]
    actions: Actions


class ScheduleFilterListModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
