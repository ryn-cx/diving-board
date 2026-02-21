# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Series(BaseModel):
    model_config = ConfigDict(extra="forbid")
    series_id: int = Field(..., alias="seriesId")
    title: str


class Item(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str
    long_description: str = Field(..., alias="longDescription")
    season_number: int = Field(..., alias="seasonNumber")
    episode_count: int = Field(..., alias="episodeCount")
    id: int
    series: Series


class Paging(BaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")


class Seasons(BaseModel):
    model_config = ConfigDict(extra="forbid")
    items: list[Item]
    paging: Paging


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    type: str
    tab: str
    series: Series
    season_id: int = Field(..., alias="seasonId")
    seasons: Seasons


class SeasonSeriesModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
