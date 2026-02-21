# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Mobile(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Tablet(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    mobile: Mobile
    tablet: Tablet


class SeasonTextBlockModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
    style: Style
