# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from uuid import UUID

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field, NaiveDatetime, field_serializer


class Attributes3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class Icon(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    from_: NaiveDatetime = Field(..., alias="from")

    @field_serializer("from_")
    def serialize_from_(self, value: NaiveDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M")


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    icon: Icon
    action: Action


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str


class Forward(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2
    style: Style


class Attributes5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class Icon1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes5


class Action1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    icon: Icon1
    action: Action1


class Back(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4
    style: Style


class Attributes6(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    format: str


class Style2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: float


class Text(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes6
    style: Style2


class Attributes8(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class AfterElement(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes8


class Action2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str


class Attributes7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    type: str
    is_small: bool = Field(..., alias="isSmall")
    after_element: AfterElement = Field(..., alias="afterElement")
    action: Action2


class Style3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: float


class Button(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes7
    style: Style3


class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    forward: Forward | None = None
    back: Back | None = None
    text: Text | None = None
    buttons: list[Button] | None = None


class Style4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    gap: str


class Element1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style4 | None = None


class Attributes9(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Style5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int
    color: str


class Title(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes9
    style: Style5


class Attributes11(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    number_of_lines: int = Field(..., alias="numberOfLines")


class Style6(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str


class Title1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes11
    style: Style6


class Option(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    filter_key: str = Field(..., alias="filterKey")
    is_active: bool = Field(..., alias="isActive")
    text: str
    format: str
    value: str


class Attributes10(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title1
    filter_key: str = Field(..., alias="filterKey")
    options: list[Option]


class Filter(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes10


class Data2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data2


class Reset(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    text: str
    action: Action3


class Action4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data2


class Apply(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    text: str
    action: Action4


class Data4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    last_seen: str = Field(..., alias="lastSeen")


class Next(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data4


class Actions(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    reset: Reset | None = None
    apply: Apply | None = None
    next: Next | None = None


class Attributes13(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: NaiveDatetime
    format: str

    @field_serializer("text")
    def serialize_text(self, value: NaiveDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M")


class Style7(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: float


class Title2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes13
    style: Style7


class Attributes15(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str
    width: int
    height: int


class HeaderItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes15


class Attributes19(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    format: str | None = None


class Style8(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str | None = None


class Text1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes19
    style: Style8


class Attributes20(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class Icon2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes20


class Attributes18(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: Text1
    icon: Icon2 | None = None
    type: str


class Style9(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str


class Tag(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes18 | None = None
    style: Style9 | None = None


class Attributes17(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str | None = None
    format: str | None = None
    number_of_lines: int | None = Field(None, alias="numberOfLines")
    tags: list[Tag] | None = None
    separator: bool | None = None


class Style10(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str


class Element2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes17
    style: Style10 | None = None


class Attributes16(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: list[Element2]
    type: str


class Style11(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    align: str


class ContentItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes16
    style: Style11


class ComputedRelease(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    scheduled_at: AwareDatetime = Field(..., alias="scheduledAt")
    computed_state: str = Field(..., alias="computedState")
    state: str
    type: str
    description: str


class Data5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    title: str
    access_level: str = Field(..., alias="accessLevel")
    online_playback: str = Field(..., alias="onlinePlayback")
    id: str
    computed_releases: list[ComputedRelease] = Field(..., alias="computedReleases")


class Action5(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data5


class Attributes14(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    has_initial_focus: bool = Field(..., alias="hasInitialFocus")
    type: str
    header: list[HeaderItem]
    content: list[ContentItem]
    grouping_data: bool = Field(..., alias="groupingData")
    action: Action5


class Card(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes14


class Attributes12(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title2
    cards: list[Card]
    type: str


class Group(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    id: NaiveDatetime
    attributes: Attributes12

    @field_serializer("id")
    def serialize_id(self, value: NaiveDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M")


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: list[Element1] | None = None
    title: Title | None = None
    filters: list[Filter] | None = None
    actions: Actions | None = None
    groups: list[Group] | None = None


class Element(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes


class Headers(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    x_api_key: UUID = Field(..., alias="x-api-key")
    origin: str = Field(..., alias="Origin")
    referer: str = Field(..., alias="Referer")
    realm: str = Field(..., alias="Realm")


class Params(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    timezone: str
    groups_per_page: int = Field(..., alias="groupsPerPage")
    items_per_group: int = Field(..., alias="itemsPerGroup")
    from_: NaiveDatetime = Field(None, alias="from")
    last_seen: str | None = Field(None, alias="lastSeen")

    @field_serializer("from_")
    def serialize_from_(self, value: NaiveDatetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M:%S")


class DivingBoard(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    headers: Headers
    params: Params


class ScheduleModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str | None = None
    layout: str
    elements: list[Element]
    diving_board: DivingBoard
