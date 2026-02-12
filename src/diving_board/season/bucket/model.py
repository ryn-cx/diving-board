# ruff: noqa: COM812, D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ContentDownload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    permission: str


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    access_level: str = Field(..., alias="accessLevel")
    type: str
    content_download: ContentDownload = Field(..., alias="contentDownload")
    description: str
    long_description: str = Field(..., alias="longDescription")
    watch_status: str = Field(..., alias="watchStatus")
    id: int
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
    duration: int | None = None
    thumbnail_url: str | None = Field(None, alias="thumbnailUrl")
    max_height: int | None = Field(None, alias="maxHeight")
    online_playback: str | None = Field(None, alias="onlinePlayback")
    computed_releases: list[None] | None = Field(None, alias="computedReleases")


class Paging(BaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")
    last_seen: int | str = Field(..., alias="lastSeen")


class GroupName(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    items: list[Item]
    tab: str
    season_id: int = Field(..., alias="seasonId")
    bucket_title: str = Field(..., alias="bucketTitle")
    series_id: int = Field(..., alias="seriesId")
    paging: Paging
    group_name: GroupName | None = Field(None, alias="groupName")
    id: int | None = None
    row_position: int | None = Field(None, alias="rowPosition")


class SeasonBucketModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
