from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data

class Attributes2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str | None = None
    width: int | None = None
    height: int | None = None
    border_radius: int = Field(..., alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes2

class Attributes3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    number_of_lines: int = Field(..., alias='numberOfLines')

class Style(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color: str
    size: str

class ContentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes3
    style: Style

class ComputedRelease(BaseModel):
    model_config = ConfigDict(defer_build=True)
    scheduled_at: AwareDatetime = Field(..., alias='scheduledAt')
    computed_state: str = Field(..., alias='computedState')
    state: str
    type: str
    description: str

class Data1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    title: str
    access_level: str = Field(..., alias='accessLevel')
    id: str
    computed_releases: list[ComputedRelease] = Field(..., alias='computedReleases')
    online_playback: str | None = Field(None, alias='onlinePlayback')

class Action1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data1

class Attributes1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    has_initial_focus: bool = Field(..., alias='hasInitialFocus')
    header: list[HeaderItem]
    content: list[ContentItem]
    action: Action1

class Card(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes1

class Data2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data2

class Next(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    label: str
    action: Action2

class Actions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    next: Next

class Attributes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    placeholder: str | None = None
    placeholder_label: str | None = Field(None, alias='placeholderLabel')
    value: str | None = None
    action: Action | None = None
    is_fallback_cards_enabled: bool | None = Field(None, alias='isFallbackCardsEnabled')
    gap: int | None = None
    disable_force_focus: bool | None = Field(None, alias='disableForceFocus')
    query: str | None = None
    cards: list[Card] | None = None
    type: str | None = None
    actions: Actions | None = None
    show_fallback_cards: bool | None = Field(None, alias='showFallbackCards')
    empty_title: str | None = Field(None, alias='emptyTitle')
    empty_description: str | None = Field(None, alias='emptyDescription')

class Style1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size: int

class Element(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    field_zone: str = Field(..., alias='$zone')
    attributes: Attributes
    style: Style1 | None = None

class SearchModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    elements: list[Element]
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
