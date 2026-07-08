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
    id: int
    video_id: int = Field(..., alias="videoId")
    online_playback: str = Field(..., alias="onlinePlayback")
    access_level: str = Field(..., alias="accessLevel")
    title: str
    type: str


class Action1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    type: str
    has_initial_focus: bool = Field(..., alias="hasInitialFocus")
    icon: str
    action: Action1


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    flex_shrink: int = Field(..., alias="flexShrink")


class Element(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4
    style: Style


class Attributes3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: list[Element]


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Attributes6(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str


class Tag(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes6 | None = None


class Data1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    type: str


class Action2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data1


class Attributes7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    text: str
    label: str
    icon: str
    action: Action2


class Button(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes7


class Attributes5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str | None = None
    tags: list[Tag] | None = None
    buttons: list[Button] | None = None


class ContentItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes5


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    header: Header
    image: Image
    actions: list[Action]
    content: list[ContentItem]


class PlaylistHeroModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
