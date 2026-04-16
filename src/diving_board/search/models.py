# ruff: noqa: TC003, D100, D101
from __future__ import annotations

from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str
    size: int


class BeforeElement(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class AfterElement(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3


class Action1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str


class Attributes2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    type: str
    is_small: bool = Field(..., alias="isSmall")
    before_element: BeforeElement | None = Field(None, alias="beforeElement")
    after_element: AfterElement = Field(..., alias="afterElement")
    hide_text_on_mobile: bool | None = Field(None, alias="hideTextOnMobile")
    action: Action1


class Style(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str


class Button(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2
    style: Style


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    buttons: list[Button]


class Style1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    gap: str


class ButtonList(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1
    style: Style1


class Attributes5(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str


class Style2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: str
    color: str


class Title(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes5
    style: Style2


class Attributes7(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    number_of_lines: int = Field(..., alias="numberOfLines")


class Title1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes7
    style: Style2


class Option(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    filter_key: str = Field(..., alias="filterKey")
    is_active: bool = Field(..., alias="isActive")
    label: str | None = None
    format: str
    value: str
    text: str | None = None


class Attributes6(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Title1
    filter_key: str = Field(..., alias="filterKey")
    options: list[Option]


class Filter(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes6


class Action2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Reset(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action2


class Action3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Apply(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action3


class Action4(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Next(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action4


class Actions(BaseModel):
    model_config = ConfigDict(extra="forbid")
    reset: Reset | None = None
    apply: Apply | None = None
    next: Next | None = None


class Option1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    field: str
    direction: str
    is_active: bool = Field(..., alias="isActive")


class Attributes9(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str | None = None
    width: int | None = None
    height: int | None = None
    border_radius: int = Field(..., alias="borderRadius")
    access_level: str | None = Field(None, alias="accessLevel")


class HeaderItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes9


class Token(BaseModel):
    model_config = ConfigDict(extra="forbid")
    key: str
    value: str


class Attributes11(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str | None = None
    size: int | None = None
    text: str | None = None
    label: str | None = None
    tokens: list[Token] | None = None
    number_of_lines: int | None = Field(None, alias="numberOfLines")


class Style4(BaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: str


class Element1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes11
    style: Style4 | None = None


class Attributes10(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str | None = None
    number_of_lines: int | None = Field(None, alias="numberOfLines")
    type: str | None = None
    elements: list[Element1] | None = None
    label: str | None = None
    tokens: list[Token] | None = None


class Style5(BaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: str
    text_align: str = Field(..., alias="textAlign")


class ContentItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes10
    style: Style5 | None = None


class Data4(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    title: str
    access_level: str = Field(..., alias="accessLevel")
    id: str
    computed_releases: list[None] = Field(..., alias="computedReleases")


class Action5(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data4


class Attributes8(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    has_initial_focus: bool = Field(..., alias="hasInitialFocus")
    force_horizontal_mobile: bool = Field(..., alias="forceHorizontalMobile")
    header: list[HeaderItem]
    content: list[ContentItem]
    action: Action5


class Card(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes8


class Attributes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    placeholder: str | None = None
    placeholder_label: str | None = Field(None, alias="placeholderLabel")
    value: str | None = None
    action: Action | None = None
    button_list: ButtonList | None = Field(None, alias="buttonList")
    title: Title | None = None
    filters: list[Filter] | None = None
    actions: Actions | None = None
    options: list[Option1] | None = None
    query: str | None = None
    cards: list[Card] | None = None
    type: str | None = None


class Style6(BaseModel):
    model_config = ConfigDict(extra="forbid")
    size: int


class Element(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
    style: Style6 | None = None


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    x_api_key: UUID = Field(..., alias="x-api-key")
    origin: str = Field(..., alias="Origin")
    referer: str = Field(..., alias="Referer")
    realm: str = Field(..., alias="Realm")


class Params(BaseModel):
    model_config = ConfigDict(extra="forbid")
    query: str
    timezone: str


class DivingBoard(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str
    timestamp: AwareDatetime
    headers: Headers
    params: Params


class SearchModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: list[Element]
    diving_board: DivingBoard
