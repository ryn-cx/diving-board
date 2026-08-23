from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, Field
from typing import Any

class Data(BaseModel):
    url: str

class Action(BaseModel):
    type: str
    data: Data

class Attributes2(BaseModel):
    source: str | None = None
    width: int | None = None
    height: int | None = None
    border_radius: int = Field(..., alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes2

class Attributes3(BaseModel):
    text: str
    number_of_lines: int = Field(..., alias='numberOfLines')

class Style(BaseModel):
    color: str
    size: str

class ContentItem(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes3
    style: Style

class Data1(BaseModel):
    type: str
    title: str
    access_level: str = Field(..., alias='accessLevel')
    id: str
    computed_releases: list[None] = Field(..., alias='computedReleases')
    online_playback: str | None = Field(None, alias='onlinePlayback')

class Action1(BaseModel):
    type: str
    data: Data1

class Attributes1(BaseModel):
    type: str
    has_initial_focus: bool = Field(..., alias='hasInitialFocus')
    header: list[HeaderItem]
    content: list[ContentItem]
    action: Action1

class Card(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes1

class Attributes(BaseModel):
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
    show_fallback_cards: bool | None = Field(None, alias='showFallbackCards')
    empty_title: str | None = Field(None, alias='emptyTitle')
    empty_description: str | None = Field(None, alias='emptyDescription')

class Style1(BaseModel):
    size: int

class Element(BaseModel):
    field_type: str = Field(..., alias='$type')
    field_zone: str = Field(..., alias='$zone')
    attributes: Attributes
    style: Style1 | None = None

class SearchModel(BaseModel):
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
