# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str


class Header(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1


class Attributes2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str


class Image(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    access_level: str = Field(..., alias="accessLevel")
    licence_ids: list[int] = Field(..., alias="licenceIds")
    id: int
    title: str
    type: str


class Action1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    has_initial_focus: bool = Field(..., alias="hasInitialFocus")
    text: str
    label: str
    icon: str
    action: Action1


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Attributes5(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str | None = None


class Tag(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes5


class Data1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    title: str
    type: str


class Action2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data1


class Attributes6(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    text: str
    label: str
    icon: str
    action: Action2


class Button(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes6


class Attributes4(BaseModel):
    model_config = ConfigDict(extra="forbid")
    tags: list[Tag] | None = None
    text: str | None = None
    id: int | None = None
    progress: None = None
    duration: int | None = None
    watch_status: str | None = Field(None, alias="watchStatus")
    buttons: list[Button] | None = None


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class ContentItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4
    style: Style | None = None


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    header: Header
    image: Image
    actions: list[Action]
    content: list[ContentItem]


class VodHeroModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
