# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Mobile(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Tablet(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    mobile: Mobile
    tablet: Tablet


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class VodTextBlockModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    style: Style
    attributes: Attributes
