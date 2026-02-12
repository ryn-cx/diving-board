# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    tab: str


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    id: int
    active_tab: str = Field(..., alias="activeTab")
    items: list[Item]


class Desktop(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Tv(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    desktop: Desktop
    tv: Tv


class VodTabsModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
    style: Style
