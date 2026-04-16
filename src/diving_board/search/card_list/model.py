# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Attributes2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str | None = None
    width: int | None = None
    height: int | None = None
    border_radius: int = Field(..., alias="borderRadius")
    access_level: str | None = Field(None, alias="accessLevel")


class HeaderItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2


class Token(BaseModel):
    model_config = ConfigDict(extra="forbid")
    key: str
    value: str


class Attributes4(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str | None = None
    size: int | None = None
    text: str | None = None
    label: str | None = None
    tokens: list[Token] | None = None
    number_of_lines: int | None = Field(None, alias="numberOfLines")


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: str


class Element(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4
    style: Style | None = None


class Attributes3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str | None = None
    number_of_lines: int | None = Field(None, alias="numberOfLines")
    type: str | None = None
    elements: list[Element] | None = None
    label: str | None = None
    tokens: list[Token] | None = None


class Style1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: str
    text_align: str = Field(..., alias="textAlign")


class ContentItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3
    style: Style1 | None = None


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    title: str
    access_level: str = Field(..., alias="accessLevel")
    id: str
    computed_releases: list[None] = Field(..., alias="computedReleases")


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    has_initial_focus: bool = Field(..., alias="hasInitialFocus")
    force_horizontal_mobile: bool = Field(..., alias="forceHorizontalMobile")
    header: list[HeaderItem]
    content: list[ContentItem]
    action: Action


class Card(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1


class Data1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data1


class Next(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action1


class Actions(BaseModel):
    model_config = ConfigDict(extra="forbid")
    next: Next


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    query: str
    cards: list[Card]
    type: str
    actions: Actions | None = None


class SearchCardListModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
