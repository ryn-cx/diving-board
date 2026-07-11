# TODO: Validate
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class BeforeElement(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class AfterElement(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Action1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str


class Attributes2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    type: str
    is_small: bool = Field(..., alias="isSmall")
    before_element: BeforeElement | None = Field(None, alias="beforeElement")
    after_element: AfterElement = Field(..., alias="afterElement")
    hide_text_on_mobile: bool | None = Field(None, alias="hideTextOnMobile")
    action: Action1


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str


class Button(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2
    style: Style


class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    buttons: list[Button]


class Style1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    gap: str


class ButtonList(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style1


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    placeholder: str
    placeholder_label: str = Field(..., alias="placeholderLabel")
    value: str
    action: Action
    button_list: ButtonList | None = Field(None, alias="buttonList")


class Style2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int


class SearchInputModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
    style: Style2
