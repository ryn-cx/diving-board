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
    title: str | None = None
    access_level: str | None = Field(None, alias="accessLevel")
    type: str | None = None
    content_download: ContentDownload | None = Field(None, alias="contentDownload")
    description: str | None = None
    long_description: str | None = Field(None, alias="longDescription")
    duration: int | None = None
    thumbnail_url: str | None = Field(None, alias="thumbnailUrl")
    max_height: int | None = Field(None, alias="maxHeight")
    online_playback: str | None = Field(None, alias="onlinePlayback")
    computed_releases: list[None] | None = Field(None, alias="computedReleases")
    watch_status: str | None = Field(None, alias="watchStatus")
    id: int | None = None
    cover_url: str | None = Field(None, alias="coverUrl")
    season_count: str | None = Field(None, alias="seasonCount")
    small_cover_url: str | None = Field(None, alias="smallCoverUrl")
    poster_url: str | None = Field(None, alias="posterUrl")
    favourite: bool | None = None
    favourite_channel: str | None = Field(None, alias="favouriteChannel")
    has_permission: bool | None = Field(None, alias="hasPermission")
    is_related: bool | None = Field(None, alias="isRelated")
    has_permission_granted_on_sign_in: bool | None = Field(
        None, alias="hasPermissionGrantedOnSignIn"
    )
    vod_count: str | None = Field(None, alias="vodCount")


class Series(BaseModel):
    model_config = ConfigDict(extra="forbid")
    series_id: int = Field(..., alias="seriesId")
    title: str


class Item1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str
    long_description: str = Field(..., alias="longDescription")
    season_number: int = Field(..., alias="seasonNumber")
    episode_count: int = Field(..., alias="episodeCount")
    id: int
    series: Series


class Paging(BaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")


class Seasons(BaseModel):
    model_config = ConfigDict(extra="forbid")
    items: list[Item1]
    paging: Paging


class Paging1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")
    last_seen: int | str = Field(..., alias="lastSeen")


class GroupName(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    header: Header | None = None
    image: Image | None = None
    actions: list[Action] | None = None
    content: list[ContentItem] | None = None
    id: int | None = None
    type: str | None = None
    active_tab: str | None = Field(None, alias="activeTab")
    items: list[Item] | None = None
    tab: str | None = None
    series: Series | None = None
    season_id: int | None = Field(None, alias="seasonId")
    seasons: Seasons | None = None
    row_position: int | None = Field(None, alias="rowPosition")
    bucket_title: str | None = Field(None, alias="bucketTitle")
    series_id: int | None = Field(None, alias="seriesId")
    paging: Paging1 | None = None
    text: str | None = None
    label: str | None = None
    group_name: GroupName | None = Field(None, alias="groupName")


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


class Style(BaseModel):
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
    style: Style | None = None


class CurrentSeason(BaseModel):
    model_config = ConfigDict(extra="forbid")
    season_id: int = Field(..., alias="seasonId")
    title: str


class CurrentVod(BaseModel):
    model_config = ConfigDict(extra="forbid")
    season_id: int = Field(..., alias="seasonId")
    title: str


class Metadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    series: Series
    current_season: CurrentSeason = Field(..., alias="currentSeason")
    current_vod: CurrentVod = Field(..., alias="currentVod")


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


class SeasonModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    layout: str
    elements: list[Element]
    metadata: Metadata
    diving_board: DivingBoard
