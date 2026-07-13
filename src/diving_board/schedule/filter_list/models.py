# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field


class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int
    color: str


class Title(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style


class Attributes3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    number_of_lines: int = Field(..., alias="numberOfLines")


class Style1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str


class Title1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3
    style: Style1


class Option(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    filter_key: str = Field(..., alias="filterKey")
    is_active: bool = Field(..., alias="isActive")
    text: str
    format: str
    value: str


class Attributes2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title1
    filter_key: str = Field(..., alias="filterKey")
    options: list[Option]


class Filter(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Reset(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    text: str
    action: Action


class Action1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Apply(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    text: str
    action: Action1


class Actions(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    reset: Reset
    apply: Apply


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title
    filters: list[Filter]
    actions: Actions


class ScheduleFilterListModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
