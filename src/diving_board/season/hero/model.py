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


class Token(BaseModel):
    model_config = ConfigDict(extra="forbid")
    key: str
    value: str


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    video_id: int = Field(..., alias="videoId")
    online_playback: str = Field(..., alias="onlinePlayback")
    access_level: str = Field(..., alias="accessLevel")
    series_id: int = Field(..., alias="seriesId")
    title: str
    type: str


class Action1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    has_initial_focus: bool = Field(..., alias="hasInitialFocus")
    text: str
    label: str
    tokens: list[Token]
    type: str
    icon: str
    action: Action1


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Attributes5(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str


class Tag(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes5


class Data1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    type: str
    universal_link: str | None = Field(None, alias="universalLink")
    tracking_parameters: list[None] | None = Field(None, alias="trackingParameters")
    title: str


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
    buttons: list[Button] | None = None


class ContentItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    header: Header
    image: Image
    actions: list[Action]
    content: list[ContentItem]


class SeasonHeroModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
