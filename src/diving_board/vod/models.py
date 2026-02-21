# ruff: noqa: COM812, TC003, D100, D101
from __future__ import annotations

from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


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


class Data2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    tab: str


class Action3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data2


class Attributes7(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action3


class ContentDownload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    permission: str


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str | None = Field(None, alias="$type")
    attributes: Attributes7 | None = None
    id: int | None = None
    type: str | None = None
    title: str | None = None
    description: str | None = None
    long_description: str | None = Field(None, alias="longDescription")
    content_download: ContentDownload | None = Field(None, alias="contentDownload")
    cover_url: str | None = Field(None, alias="coverUrl")
    small_cover_url: str | None = Field(None, alias="smallCoverUrl")
    season_count: str | None = Field(None, alias="seasonCount")
    poster_url: str | None = Field(None, alias="posterUrl")
    access_level: str | None = Field(None, alias="accessLevel")
    favourite: bool | None = None
    watch_status: str | None = Field(None, alias="watchStatus")
    favourite_channel: str | None = Field(None, alias="favouriteChannel")
    has_permission: bool | None = Field(None, alias="hasPermission")
    is_related: bool | None = Field(None, alias="isRelated")
    has_permission_granted_on_sign_in: bool | None = Field(
        None, alias="hasPermissionGrantedOnSignIn"
    )


class GroupName(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Paging(BaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")
    last_seen: str = Field(..., alias="lastSeen")


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    header: Header | None = None
    image: Image | None = None
    actions: list[Action] | None = None
    content: list[ContentItem] | None = None
    type: str | None = None
    id: int | None = None
    active_tab: str | None = Field(None, alias="activeTab")
    items: list[Item] | None = None
    text: str | None = None
    label: str | None = None
    tab: str | None = None
    bucket_title: str | None = Field(None, alias="bucketTitle")
    group_name: GroupName | None = Field(None, alias="groupName")
    paging: Paging | None = None


class Desktop(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Tv(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Mobile(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Tablet(BaseModel):
    model_config = ConfigDict(extra="forbid")
    display: str


class Style1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    desktop: Desktop | None = None
    tv: Tv | None = None
    mobile: Mobile | None = None
    tablet: Tablet | None = None


class Element(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
    style: Style1 | None = None


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    x_api_key: UUID = Field(..., alias="x-api-key")
    origin: str = Field(..., alias="Origin")
    referer: str = Field(..., alias="Referer")
    realm: str = Field(..., alias="Realm")


class Params(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    id: int
    timezone: str


class DivingBoard(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    headers: Headers
    params: Params


class VodModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: list[Element]
    diving_board: DivingBoard
