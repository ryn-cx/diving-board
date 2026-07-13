# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Attributes3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class Icon(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    from_: str = Field(..., alias="from")


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    icon: Icon
    action: Action


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str


class Forward(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2
    style: Style


class Attributes5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class Icon1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes5


class Action1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    icon: Icon1
    action: Action1


class Back(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4
    style: Style


class Attributes6(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    format: str


class Style2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: float


class Text(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes6
    style: Style2


class Attributes8(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class AfterElement(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes8


class Action2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str


class Attributes7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    type: str
    is_small: bool = Field(..., alias="isSmall")
    after_element: AfterElement = Field(..., alias="afterElement")
    action: Action2


class Style3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: float


class Button(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes7
    style: Style3


class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    forward: Forward | None = None
    back: Back | None = None
    text: Text | None = None
    buttons: list[Button] | None = None


class Style4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    gap: str


class Element(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style4 | None = None


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: list[Element]


class ScheduleGridBlockModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
