# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class PrecedingSeason(GAPIBaseModel):
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


class FollowingSeason(GAPIBaseModel):
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


class PrecedingItem(GAPIBaseModel):
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


class FollowingItem(GAPIBaseModel):
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


class WatchOrder(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    preceding: list[PrecedingItem]
    following: list[FollowingItem]


class SeriesAdjacentToModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    preceding_seasons: list[PrecedingSeason] = Field(..., alias="precedingSeasons")
    following_seasons: list[FollowingSeason] = Field(..., alias="followingSeasons")
    watch_order: WatchOrder = Field(..., alias="watchOrder")
