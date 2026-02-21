# ruff: noqa: D100, D101, D102
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, NaiveDatetime, field_serializer


class Attributes3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class Icon(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    from_: NaiveDatetime = Field(..., alias="from")

    @field_serializer("from_")
    def serialize_from_(self, value: NaiveDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M")


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    icon: Icon
    action: Action


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str


class Forward(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2
    style: Style


class Attributes5(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class Icon1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes5


class Action1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes4(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    icon: Icon1
    action: Action1


class Back(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4
    style: Style


class Attributes6(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    format: str


class Style2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: float


class Text(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes6
    style: Style2


class Attributes8(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class AfterElement(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes8


class Action2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str


class Attributes7(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    type: str
    is_small: bool = Field(..., alias="isSmall")
    after_element: AfterElement = Field(..., alias="afterElement")
    action: Action2


class Style3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: float


class Button(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes7
    style: Style3


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    forward: Forward | None = None
    back: Back | None = None
    text: Text | None = None
    buttons: list[Button] | None = None


class Style4(BaseModel):
    model_config = ConfigDict(extra="forbid")
    gap: str


class Element(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style4 | None = None


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: list[Element]


class ScheduleGridBlockModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
