# ruff: noqa: D100, D101
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    tab: str


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    type: str
    active_tab: str = Field(..., alias="activeTab")
    items: list[Item]


class Desktop(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Tv(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    desktop: Desktop
    tv: Tv


class SeasonTabsModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
    style: Style
