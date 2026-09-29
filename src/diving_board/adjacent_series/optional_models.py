from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class PrecedingSeason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    long_description: str | Any = Field(None, alias='longDescription', union_mode='left_to_right')
    small_cover_url: str | Any = Field(None, alias='smallCoverUrl', union_mode='left_to_right')
    cover_url: str | Any = Field(None, alias='coverUrl', union_mode='left_to_right')
    title_url: str | Any = Field(None, alias='titleUrl', union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    episode_count: int | Any = Field(None, alias='episodeCount', union_mode='left_to_right')
    displayable_tags: list[Any] | Any = Field(None, alias='displayableTags', union_mode='left_to_right')
    upcoming_releases: list[Any] | Any = Field(None, alias='upcomingReleases', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')

class FollowingSeason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    long_description: str | Any = Field(None, alias='longDescription', union_mode='left_to_right')
    small_cover_url: str | Any = Field(None, alias='smallCoverUrl', union_mode='left_to_right')
    cover_url: str | Any = Field(None, alias='coverUrl', union_mode='left_to_right')
    title_url: str | Any = Field(None, alias='titleUrl', union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    episode_count: int | Any = Field(None, alias='episodeCount', union_mode='left_to_right')
    displayable_tags: list[Any] | Any = Field(None, alias='displayableTags', union_mode='left_to_right')
    upcoming_releases: list[Any] | Any = Field(None, alias='upcomingReleases', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')

class PrecedingItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    long_description: str | Any = Field(None, alias='longDescription', union_mode='left_to_right')
    small_cover_url: str | Any = Field(None, alias='smallCoverUrl', union_mode='left_to_right')
    cover_url: str | Any = Field(None, alias='coverUrl', union_mode='left_to_right')
    title_url: str | Any = Field(None, alias='titleUrl', union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    episode_count: int | Any = Field(None, alias='episodeCount', union_mode='left_to_right')
    displayable_tags: list[Any] | Any = Field(None, alias='displayableTags', union_mode='left_to_right')
    upcoming_releases: list[Any] | Any = Field(None, alias='upcomingReleases', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')

class FollowingItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    long_description: str | Any = Field(None, alias='longDescription', union_mode='left_to_right')
    small_cover_url: str | Any = Field(None, alias='smallCoverUrl', union_mode='left_to_right')
    cover_url: str | Any = Field(None, alias='coverUrl', union_mode='left_to_right')
    title_url: str | Any = Field(None, alias='titleUrl', union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    episode_count: int | Any = Field(None, alias='episodeCount', union_mode='left_to_right')
    displayable_tags: list[Any] | Any = Field(None, alias='displayableTags', union_mode='left_to_right')
    upcoming_releases: list[Any] | Any = Field(None, alias='upcomingReleases', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')

class WatchOrder(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    preceding: list[PrecedingItem] | Any = Field(default=None, union_mode='left_to_right')
    following: list[FollowingItem] | Any = Field(default=None, union_mode='left_to_right')

class AdjacentSeriesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    preceding_seasons: list[PrecedingSeason] | Any = Field(None, alias='precedingSeasons', union_mode='left_to_right')
    following_seasons: list[FollowingSeason] | Any = Field(None, alias='followingSeasons', union_mode='left_to_right')
    watch_order: WatchOrder | Any = Field(None, alias='watchOrder', union_mode='left_to_right')
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
