# ruff: noqa: D100, D101
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str


class Header(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1


class Attributes2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str


class Image(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    access_level: str = Field(..., alias="accessLevel")
    licence_ids: list[int] = Field(..., alias="licenceIds")
    id: int
    title: str
    type: str


class Action1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    has_initial_focus: bool = Field(..., alias="hasInitialFocus")
    text: str
    label: str
    icon: str
    action: Action1


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Attributes5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str | None = None


class Tag(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes5


class Data1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    title: str
    type: str


class Action2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data1


class Attributes6(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    text: str
    label: str
    icon: str
    action: Action2


class Button(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes6


class Attributes4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    tags: list[Tag] | None = None
    text: str | None = None
    id: int | None = None
    progress: None = None
    duration: int | None = None
    watch_status: str | None = Field(None, alias="watchStatus")
    buttons: list[Button] | None = None


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class ContentItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4
    style: Style | None = None


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    header: Header
    image: Image
    actions: list[Action]
    content: list[ContentItem]


class VodHeroModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
