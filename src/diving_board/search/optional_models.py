from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    data: Data | None = None

class Attributes2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    source: str | None = None
    width: int | None = None
    height: int | None = None
    border_radius: int | None = Field(None, alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes2 | None = None

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    number_of_lines: int | None = Field(None, alias='numberOfLines')

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore')
    color: str | None = None
    size: str | None = None

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes3 | None = None
    style: Style | None = None

class Data1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    title: str | None = None
    access_level: str | None = Field(None, alias='accessLevel')
    id: str | None = None
    computed_releases: list[Any] | None = Field(None, alias='computedReleases')
    online_playback: str | None = Field(None, alias='onlinePlayback')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    data: Data1 | None = None

class Attributes1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    has_initial_focus: bool | None = Field(None, alias='hasInitialFocus')
    header: list[HeaderItem] | None = None
    content: list[ContentItem] | None = None
    action: Action1 | None = None

class Card(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes1 | None = None

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore')
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
    model_config = ConfigDict(extra='ignore')
    size: int | None = None

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    field_zone: str | None = Field(None, alias='$zone')
    attributes: Attributes | None = None
    style: Style1 | None = None

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    source: str | None = None
    elements: list[Element] | None = None
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
