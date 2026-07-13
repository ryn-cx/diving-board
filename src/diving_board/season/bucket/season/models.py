# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class ContentDownload(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    permission: str


class Item(GAPIBaseModel):
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


class Paging(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")
    last_seen: int = Field(..., alias="lastSeen")


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    tab: str
    row_position: int = Field(..., alias="rowPosition")
    bucket_title: str = Field(..., alias="bucketTitle")
    series_id: int = Field(..., alias="seriesId")
    season_id: int = Field(..., alias="seasonId")
    id: int
    items: list[Item]
    paging: Paging


class SeasonBucketSeasonModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
