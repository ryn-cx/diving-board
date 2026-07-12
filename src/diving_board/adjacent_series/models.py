# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from uuid import UUID

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


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


class AudioLanguageCode(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    region: str
    language: str


class SubtitleLanguageCode(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    region: str
    language: str


class LocalisedValues(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    en_us: str = Field(..., alias="en_US")


class Localisations(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    localised_values: LocalisedValues = Field(..., alias="localisedValues")


class ComputedRelease(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    state: str
    computed_state: str = Field(..., alias="computedState")
    date: AwareDatetime
    scheduled_at: AwareDatetime = Field(..., alias="scheduledAt")
    type: str
    audio_language_codes: list[AudioLanguageCode] = Field(
        ...,
        alias="audioLanguageCodes",
    )
    subtitle_language_codes: list[SubtitleLanguageCode] = Field(
        ...,
        alias="subtitleLanguageCodes",
    )
    localisations: Localisations
    description: str


class UpcomingRelease(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    title: str
    description: str
    online_playback: str = Field(..., alias="onlinePlayback")
    computed_releases: list[ComputedRelease] = Field(..., alias="computedReleases")
    type: str


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
    upcoming_releases: list[UpcomingRelease] = Field(..., alias="upcomingReleases")
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


class Localisations1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    localised_values: LocalisedValues = Field(..., alias="localisedValues")


class ComputedRelease1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    state: str
    computed_state: str = Field(..., alias="computedState")
    date: AwareDatetime
    scheduled_at: AwareDatetime = Field(..., alias="scheduledAt")
    type: str
    audio_language_codes: list[AudioLanguageCode] = Field(
        ...,
        alias="audioLanguageCodes",
    )
    subtitle_language_codes: list[SubtitleLanguageCode] = Field(
        ...,
        alias="subtitleLanguageCodes",
    )
    localisations: Localisations1
    description: str


class UpcomingRelease1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    title: str
    description: str
    online_playback: str = Field(..., alias="onlinePlayback")
    computed_releases: list[ComputedRelease1] = Field(..., alias="computedReleases")
    type: str


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
    upcoming_releases: list[UpcomingRelease1] = Field(..., alias="upcomingReleases")
    id: int


class WatchOrder(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    preceding: list[PrecedingItem]
    following: list[FollowingItem]


class Headers(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    x_api_key: UUID = Field(..., alias="x-api-key")
    origin: str = Field(..., alias="Origin")
    referer: str = Field(..., alias="Referer")
    realm: str = Field(..., alias="Realm")


class Params(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int


class DivingBoard(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    headers: Headers
    params: Params


class AdjacentSeries(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    preceding_seasons: list[PrecedingSeason] | None = Field(
        None,
        alias="precedingSeasons",
    )
    following_seasons: list[FollowingSeason] | None = Field(
        None,
        alias="followingSeasons",
    )
    watch_order: WatchOrder | None = Field(None, alias="watchOrder")
    diving_board: DivingBoard | None = None
    status: int | None = None
    code: str | None = None
    messages: list[str] | None = None
    request_id: str | None = Field(None, alias="requestId")
