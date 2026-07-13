# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
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


class Attributes3(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    number_of_lines: int = Field(..., alias="numberOfLines")


class Style(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    color: str
    size: str


class ContentItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    attributes: Attributes3
    style: Style


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
    online_playback: str | None = Field(None, alias="onlinePlayback")
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
    is_fallback_cards_enabled: bool = Field(..., alias="isFallbackCardsEnabled")
    gap: int
    disable_force_focus: bool = Field(..., alias="disableForceFocus")
    show_fallback_cards: bool | None = Field(None, alias="showFallbackCards")
    empty_title: str | None = Field(None, alias="emptyTitle")
    empty_description: str | None = Field(None, alias="emptyDescription")
    query: str
    cards: list[Card]
    type: str
    actions: Actions | None = None


class SearchCardListModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_type: str = Field(..., alias="$type")
    field_zone: str = Field(..., alias="$zone")
    attributes: Attributes
