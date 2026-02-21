# ruff: noqa: TC003, D100, D101
from __future__ import annotations

from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class FollowingSeason(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str
    long_description: str = Field(..., alias="longDescription")
    small_cover_url: str = Field(..., alias="smallCoverUrl")
    cover_url: str = Field(..., alias="coverUrl")
    title_url: str = Field(..., alias="titleUrl")
    poster_url: str = Field(..., alias="posterUrl")
    season_number: int = Field(..., alias="seasonNumber")
    episode_count: int = Field(..., alias="episodeCount")
    displayable_tags: list[None] = Field(..., alias="displayableTags")
    upcoming_releases: list[None] = Field(..., alias="upcomingReleases")
    id: int


class FollowingItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str
    long_description: str = Field(..., alias="longDescription")
    small_cover_url: str = Field(..., alias="smallCoverUrl")
    cover_url: str = Field(..., alias="coverUrl")
    title_url: str = Field(..., alias="titleUrl")
    poster_url: str = Field(..., alias="posterUrl")
    season_number: int = Field(..., alias="seasonNumber")
    episode_count: int = Field(..., alias="episodeCount")
    displayable_tags: list[None] = Field(..., alias="displayableTags")
    upcoming_releases: list[None] = Field(..., alias="upcomingReleases")
    id: int


class WatchOrder(BaseModel):
    model_config = ConfigDict(extra="forbid")
    preceding: list[None]
    following: list[FollowingItem]


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    x_api_key: UUID = Field(..., alias="x-api-key")
    origin: str = Field(..., alias="Origin")
    referer: str = Field(..., alias="Referer")
    realm: str = Field(..., alias="Realm")


class Params(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int


class DivingBoard(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    headers: Headers
    params: Params


class AdjacentSeries(BaseModel):
    model_config = ConfigDict(extra="forbid")
    preceding_seasons: list[None] = Field(..., alias="precedingSeasons")
    following_seasons: list[FollowingSeason] = Field(..., alias="followingSeasons")
    watch_order: WatchOrder = Field(..., alias="watchOrder")
    diving_board: DivingBoard
