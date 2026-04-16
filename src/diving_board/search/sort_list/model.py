# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str


class Title(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style


class Option(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    field: str
    direction: str
    is_active: bool = Field(..., alias="isActive")


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    action: Action
    title: Title
    options: list[Option]


class SearchSortListModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
