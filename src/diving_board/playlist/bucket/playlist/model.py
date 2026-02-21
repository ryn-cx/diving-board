# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ContentDownload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    permission: str


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    type: str
    access_level: str = Field(..., alias="accessLevel")
    licence_ids: list[int] = Field(..., alias="licenceIds")
    description: str
    long_description: str = Field(..., alias="longDescription")
    thumbnail_url: str = Field(..., alias="thumbnailUrl")
    max_height: int = Field(..., alias="maxHeight")
    computed_releases: list[None] = Field(..., alias="computedReleases")
    poster_url: str = Field(..., alias="posterUrl")
    duration: str
    content_download: ContentDownload = Field(..., alias="contentDownload")
    watch_status: str = Field(..., alias="watchStatus")
    title: str


class Paging(BaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")
    last_seen: int = Field(..., alias="lastSeen")


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    type: str
    items: list[Item]
    tab: str
    row_position: int = Field(..., alias="rowPosition")
    bucket_title: str = Field(..., alias="bucketTitle")
    paging: Paging


class PlaylistBucketPlaylistModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
