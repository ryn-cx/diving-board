# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field, NaiveDatetime, field_serializer


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    last_seen: str = Field(..., alias="lastSeen")


class Next(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Actions(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    next: Next


class Attributes2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: NaiveDatetime
    format: str

    @field_serializer("text")
    def serialize_text(self, value: NaiveDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M")


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: float


class Title(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2
    style: Style


class Attributes4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str
    width: int
    height: int


class HeaderItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4


class Attributes8(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    format: str | None = None


class Style1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str | None = None


class Text(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes8
    style: Style1


class Attributes9(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class Icon(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes9


class Attributes7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: Text
    icon: Icon | None = None
    type: str


class Style2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str


class Tag(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes7 | None = None
    style: Style2 | None = None


class Attributes6(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str | None = None
    format: str | None = None
    number_of_lines: int | None = Field(None, alias="numberOfLines")
    tags: list[Tag] | None = None
    separator: bool | None = None


class Style3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str


class Element(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes6
    style: Style3 | None = None


class Attributes5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: list[Element]
    type: str


class Style4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    align: str


class ContentItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes5
    style: Style4


class ComputedRelease(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    scheduled_at: AwareDatetime = Field(..., alias="scheduledAt")
    computed_state: str = Field(..., alias="computedState")
    state: str
    type: str
    description: str


class Data1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    title: str
    access_level: str = Field(..., alias="accessLevel")
    online_playback: str = Field(..., alias="onlinePlayback")
    id: str
    computed_releases: list[ComputedRelease] = Field(..., alias="computedReleases")


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data1


class Attributes3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    has_initial_focus: bool = Field(..., alias="hasInitialFocus")
    type: str
    header: list[HeaderItem]
    content: list[ContentItem]
    grouping_data: bool = Field(..., alias="groupingData")
    action: Action


class Card(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title
    cards: list[Card]
    type: str


class Group(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    id: NaiveDatetime
    attributes: Attributes1

    @field_serializer("id")
    def serialize_id(self, value: NaiveDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M")


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    actions: Actions | None = None
    groups: list[Group]


class ScheduleGroupListModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
