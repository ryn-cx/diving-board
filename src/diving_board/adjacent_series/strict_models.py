from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from typing import Any

class PrecedingSeason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str
    long_description: str = Field(..., alias='longDescription')
    small_cover_url: str = Field(..., alias='smallCoverUrl')
    cover_url: str = Field(..., alias='coverUrl')
    title_url: str = Field(..., alias='titleUrl')
    poster_url: str = Field(..., alias='posterUrl')
    season_number: int = Field(..., alias='seasonNumber')
    episode_count: int = Field(..., alias='episodeCount')
    displayable_tags: list[None] = Field(..., alias='displayableTags')
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')
    id: int

class FollowingSeason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str
    long_description: str = Field(..., alias='longDescription')
    small_cover_url: str = Field(..., alias='smallCoverUrl')
    cover_url: str = Field(..., alias='coverUrl')
    title_url: str = Field(..., alias='titleUrl')
    poster_url: str = Field(..., alias='posterUrl')
    season_number: int = Field(..., alias='seasonNumber')
    episode_count: int = Field(..., alias='episodeCount')
    displayable_tags: list[None] = Field(..., alias='displayableTags')
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')
    id: int

class PrecedingItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str
    long_description: str = Field(..., alias='longDescription')
    small_cover_url: str = Field(..., alias='smallCoverUrl')
    cover_url: str = Field(..., alias='coverUrl')
    title_url: str = Field(..., alias='titleUrl')
    poster_url: str = Field(..., alias='posterUrl')
    season_number: int = Field(..., alias='seasonNumber')
    episode_count: int = Field(..., alias='episodeCount')
    displayable_tags: list[None] = Field(..., alias='displayableTags')
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')
    id: int

class FollowingItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str
    long_description: str = Field(..., alias='longDescription')
    small_cover_url: str = Field(..., alias='smallCoverUrl')
    cover_url: str = Field(..., alias='coverUrl')
    title_url: str = Field(..., alias='titleUrl')
    poster_url: str = Field(..., alias='posterUrl')
    season_number: int = Field(..., alias='seasonNumber')
    episode_count: int = Field(..., alias='episodeCount')
    displayable_tags: list[None] = Field(..., alias='displayableTags')
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')
    id: int

class WatchOrder(BaseModel):
    model_config = ConfigDict(defer_build=True)
    preceding: list[PrecedingItem]
    following: list[FollowingItem]

class AdjacentSeriesModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    preceding_seasons: list[PrecedingSeason] = Field(..., alias='precedingSeasons')
    following_seasons: list[FollowingSeason] = Field(..., alias='followingSeasons')
    watch_order: WatchOrder = Field(..., alias='watchOrder')
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
