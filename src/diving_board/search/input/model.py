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


class Attributes3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class BeforeElement(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class AfterElement(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Action1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str


class Attributes2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    type: str
    is_small: bool = Field(..., alias="isSmall")
    before_element: BeforeElement | None = Field(None, alias="beforeElement")
    after_element: AfterElement = Field(..., alias="afterElement")
    hide_text_on_mobile: bool | None = Field(None, alias="hideTextOnMobile")
    action: Action1


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str


class Button(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2
    style: Style


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    buttons: list[Button]


class Style1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    gap: str


class ButtonList(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style1


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    placeholder: str
    placeholder_label: str = Field(..., alias="placeholderLabel")
    value: str
    action: Action
    button_list: ButtonList = Field(..., alias="buttonList")


class Style2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int


class SearchInputModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
    style: Style2
