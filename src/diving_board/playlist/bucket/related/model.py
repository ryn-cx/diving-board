# ruff: noqa: D100, D101
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class ContentDownload(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    permission: str


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    type: str
    access_level: str = Field(..., alias="accessLevel")
    description: str
    long_description: str = Field(..., alias="longDescription")
    poster_url: str | None = Field(None, alias="posterUrl")
    content_download: ContentDownload = Field(..., alias="contentDownload")
    watch_status: str = Field(..., alias="watchStatus")
    title: str
    cover_url: str | None = Field(None, alias="coverUrl")
    small_cover_url: str | None = Field(None, alias="smallCoverUrl")
    season_count: str | None = Field(None, alias="seasonCount")
    favourite: bool
    favourite_channel: str = Field(..., alias="favouriteChannel")
    has_permission: bool = Field(..., alias="hasPermission")
    is_related: bool = Field(..., alias="isRelated")
    has_permission_granted_on_sign_in: bool = Field(
        ...,
        alias="hasPermissionGrantedOnSignIn",
    )
    vod_count: str | None = Field(None, alias="vodCount")
    thumbnail_url: str | None = Field(None, alias="thumbnailUrl")
    duration: str | None = None


class Paging(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")
    last_seen: str = Field(..., alias="lastSeen")


class GroupName(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    items: list[Item]
    tab: str
    bucket_title: str = Field(..., alias="bucketTitle")
    paging: Paging
    group_name: GroupName = Field(..., alias="groupName")


class PlaylistBucketRelatedModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
