# ruff: noqa: D100, D101
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
    duration: int
    thumbnail_url: str = Field(..., alias="thumbnailUrl")
    max_height: int = Field(..., alias="maxHeight")
    online_playback: str = Field(..., alias="onlinePlayback")
    computed_releases: list[None] = Field(..., alias="computedReleases")
    watch_status: str = Field(..., alias="watchStatus")
    id: int


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
    season_id: int = Field(..., alias="seasonId")
    row_position: int = Field(..., alias="rowPosition")
    bucket_title: str = Field(..., alias="bucketTitle")
    series_id: int = Field(..., alias="seriesId")
    paging: Paging


class SeasonBucketSeasonModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
