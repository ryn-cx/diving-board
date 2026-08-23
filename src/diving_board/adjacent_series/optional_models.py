from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class PrecedingSeason(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None
    long_description: str | None = Field(None, alias='longDescription')
    small_cover_url: str | None = Field(None, alias='smallCoverUrl')
    cover_url: str | None = Field(None, alias='coverUrl')
    title_url: str | None = Field(None, alias='titleUrl')
    poster_url: str | None = Field(None, alias='posterUrl')
    season_number: int | None = Field(None, alias='seasonNumber')
    episode_count: int | None = Field(None, alias='episodeCount')
    displayable_tags: list[Any] | None = Field(None, alias='displayableTags')
    upcoming_releases: list[Any] | None = Field(None, alias='upcomingReleases')
    id: int | None = None

class FollowingSeason(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None
    long_description: str | None = Field(None, alias='longDescription')
    small_cover_url: str | None = Field(None, alias='smallCoverUrl')
    cover_url: str | None = Field(None, alias='coverUrl')
    title_url: str | None = Field(None, alias='titleUrl')
    poster_url: str | None = Field(None, alias='posterUrl')
    season_number: int | None = Field(None, alias='seasonNumber')
    episode_count: int | None = Field(None, alias='episodeCount')
    displayable_tags: list[Any] | None = Field(None, alias='displayableTags')
    upcoming_releases: list[Any] | None = Field(None, alias='upcomingReleases')
    id: int | None = None

class PrecedingItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None
    long_description: str | None = Field(None, alias='longDescription')
    small_cover_url: str | None = Field(None, alias='smallCoverUrl')
    cover_url: str | None = Field(None, alias='coverUrl')
    title_url: str | None = Field(None, alias='titleUrl')
    poster_url: str | None = Field(None, alias='posterUrl')
    season_number: int | None = Field(None, alias='seasonNumber')
    episode_count: int | None = Field(None, alias='episodeCount')
    displayable_tags: list[Any] | None = Field(None, alias='displayableTags')
    upcoming_releases: list[Any] | None = Field(None, alias='upcomingReleases')
    id: int | None = None

class FollowingItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None
    long_description: str | None = Field(None, alias='longDescription')
    small_cover_url: str | None = Field(None, alias='smallCoverUrl')
    cover_url: str | None = Field(None, alias='coverUrl')
    title_url: str | None = Field(None, alias='titleUrl')
    poster_url: str | None = Field(None, alias='posterUrl')
    season_number: int | None = Field(None, alias='seasonNumber')
    episode_count: int | None = Field(None, alias='episodeCount')
    displayable_tags: list[Any] | None = Field(None, alias='displayableTags')
    upcoming_releases: list[Any] | None = Field(None, alias='upcomingReleases')
    id: int | None = None

class WatchOrder(BaseModel):
    model_config = ConfigDict(extra='ignore')
    preceding: list[PrecedingItem] | None = None
    following: list[FollowingItem] | None = None

class AdjacentSeriesModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    preceding_seasons: list[PrecedingSeason] | None = Field(None, alias='precedingSeasons')
    following_seasons: list[FollowingSeason] | None = Field(None, alias='followingSeasons')
    watch_order: WatchOrder | None = Field(None, alias='watchOrder')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
