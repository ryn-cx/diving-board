# ruff: noqa: TC003, D100, D101
from __future__ import annotations

from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    buttons: list[None]


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    gap: str


class ButtonList(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style


class Attributes2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Style1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str


class Title(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2
    style: Style1


class Action1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Reset(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action1


class Action2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Apply(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action2


class Actions(BaseModel):
    model_config = ConfigDict(extra="forbid")
    reset: Reset
    apply: Apply


class Option(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    field: str
    direction: str
    is_active: bool = Field(..., alias="isActive")


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    placeholder: str | None = None
    placeholder_label: str | None = Field(None, alias="placeholderLabel")
    value: str | None = None
    action: Action | None = None
    button_list: ButtonList | None = Field(None, alias="buttonList")
    title: Title | None = None
    filters: list[None] | None = None
    actions: Actions | None = None
    options: list[Option] | None = None
    query: str | None = None
    cards: list[None] | None = None
    type: str | None = None


class Style2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int


class Element(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
    style: Style2 | None = None


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    x_api_key: UUID = Field(..., alias="x-api-key")
    origin: str = Field(..., alias="Origin")
    referer: str = Field(..., alias="Referer")
    realm: str = Field(..., alias="Realm")


class Params(BaseModel):
    model_config = ConfigDict(extra="forbid")
    query: str
    timezone: str


class DivingBoard(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    headers: Headers
    params: Params


class SearchModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: list[Element]
    diving_board: DivingBoard
