# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class GroupName(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class ContentDownload(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    permission: str


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    type: str
    title: str
    description: str
    long_description: str = Field(..., alias="longDescription")
    content_download: ContentDownload = Field(..., alias="contentDownload")
    cover_url: str = Field(..., alias="coverUrl")
    small_cover_url: str = Field(..., alias="smallCoverUrl")
    season_count: str = Field(..., alias="seasonCount")
    poster_url: str = Field(..., alias="posterUrl")
    access_level: str = Field(..., alias="accessLevel")
    favourite: bool
    watch_status: str = Field(..., alias="watchStatus")
    favourite_channel: str = Field(..., alias="favouriteChannel")
    has_permission: bool = Field(..., alias="hasPermission")
    is_related: bool = Field(..., alias="isRelated")
    has_permission_granted_on_sign_in: bool = Field(
        ...,
        alias="hasPermissionGrantedOnSignIn",
    )


class Paging(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")
    last_seen: str = Field(..., alias="lastSeen")


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    tab: str
    type: str
    bucket_title: str = Field(..., alias="bucketTitle")
    group_name: GroupName = Field(..., alias="groupName")
    items: list[Item]
    paging: Paging


class VodBucketModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
