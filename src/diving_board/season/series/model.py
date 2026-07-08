# ruff: noqa: D100, D101
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Series(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    series_id: int = Field(..., alias="seriesId")
    title: str


class Item(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    description: str
    long_description: str = Field(..., alias="longDescription")
    season_number: int = Field(..., alias="seasonNumber")
    episode_count: int = Field(..., alias="episodeCount")
    id: int
    series: Series


class Paging(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    more_data_available: bool = Field(..., alias="moreDataAvailable")


class Seasons(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    items: list[Item]
    paging: Paging


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    type: str
    tab: str
    series: Series
    season_id: int = Field(..., alias="seasonId")
    seasons: Seasons


class SeasonSeriesModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
