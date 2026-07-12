# ruff: noqa: D100, D101
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class Attributes2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str | None = None
    width: int | None = None
    height: int | None = None
    border_radius: int = Field(..., alias="borderRadius")
    access_level: str | None = Field(None, alias="accessLevel")


class HeaderItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes2


class Token(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    key: str
    value: str


class Attributes4(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    icon: str | None = None
    size: int | None = None
    text: str | None = None
    label: str | None = None
    tokens: list[Token] | None = None
    number_of_lines: int | None = Field(None, alias="numberOfLines")


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: str


class Element(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes4
    style: Style | None = None


class Attributes3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str | None = None
    number_of_lines: int | None = Field(None, alias="numberOfLines")
    type: str | None = None
    elements: list[Element] | None = None
    label: str | None = None
    tokens: list[Token] | None = None


class Style1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: str
    text_align: str | None = Field(None, alias="textAlign")


class ContentItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3
    style: Style1 | None = None


class ComputedRelease(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    scheduled_at: AwareDatetime = Field(..., alias="scheduledAt")
    computed_state: str = Field(..., alias="computedState")
    state: str
    type: str
    description: str


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    title: str
    access_level: str = Field(..., alias="accessLevel")
    id: str
    computed_releases: list[ComputedRelease] = Field(..., alias="computedReleases")


class Action(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data


class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    has_initial_focus: bool = Field(..., alias="hasInitialFocus")
    force_horizontal_mobile: bool | None = Field(None, alias="forceHorizontalMobile")
    header: list[HeaderItem]
    content: list[ContentItem]
    action: Action


class Card(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes1


class Data1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url: str


class Action1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: Data1


class Next(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    label: str
    action: Action1


class Actions(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    next: Next


class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    query: str
    cards: list[Card]
    type: str
    actions: Actions | None = None
    is_fallback_cards_enabled: bool | None = Field(None, alias="isFallbackCardsEnabled")
    gap: int | None = None
    disable_force_focus: bool | None = Field(None, alias="disableForceFocus")
    show_fallback_cards: bool | None = Field(None, alias="showFallbackCards")
    empty_title: str | None = Field(None, alias="emptyTitle")
    empty_description: str | None = Field(None, alias="emptyDescription")


class SearchCardListModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
