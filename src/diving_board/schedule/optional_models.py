from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, NaiveDatetime

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    size: int | None = None

class Icon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes3 | None = None

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    from_: NaiveDatetime | None = Field(None, alias='from')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data | None = None

class Attributes2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    icon: Icon | None = None
    action: Action | None = None

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | None = None

class Forward(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes2 | None = None
    style: Style | None = None

class Attributes5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    size: int | None = None

class Icon1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes5 | None = None

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data | None = None

class Attributes4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    icon: Icon1 | None = None
    action: Action1 | None = None

class Back(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes4 | None = None
    style: Style | None = None

class Attributes6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    format: str | None = None

class Style2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None
    size: float | None = None

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes6 | None = None
    style: Style2 | None = None

class Attributes8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    size: int | None = None

class AfterElement(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes8 | None = None

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None

class Attributes7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    label: str | None = None
    type: str | None = None
    is_small: bool | None = Field(None, alias='isSmall')
    after_element: AfterElement | None = Field(None, alias='afterElement')
    action: Action2 | None = None

class Style3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: float | None = None

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes7 | None = None
    style: Style3 | None = None

class Attributes1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    forward: Forward | None = None
    back: Back | None = None
    text: Text | None = None
    buttons: list[Button] | None = None

class Style4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: str | None = None

class Element1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes1 | None = None
    style: Style4 | None = None

class Attributes9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    label: str | None = None

class Style5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: int | None = None
    color: str | None = None

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes9 | None = None
    style: Style5 | None = None

class Attributes11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None
    number_of_lines: int | None = Field(None, alias='numberOfLines')

class Style6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | None = None
    color: str | None = None

class Title1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes11 | None = None
    style: Style6 | None = None

class Option(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    filter_key: str | None = Field(None, alias='filterKey')
    is_active: bool | None = Field(None, alias='isActive')
    text: str | None = None
    format: str | None = None
    value: str | None = None

class Attributes10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title1 | None = None
    filter_key: str | None = Field(None, alias='filterKey')
    options: list[Option] | None = None

class Filter(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes10 | None = None

class Data2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data2 | None = None

class Reset(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None
    text: str | None = None
    action: Action3 | None = None

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data2 | None = None

class Apply(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None
    text: str | None = None
    action: Action4 | None = None

class Data4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    last_seen: str | None = Field(None, alias='lastSeen')

class Next(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data4 | None = None

class Actions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    reset: Reset | None = None
    apply: Apply | None = None
    next: Next | None = None

class Attributes13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: NaiveDatetime | None = None
    format: str | None = None

class Style7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None
    size: float | None = None

class Title2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes13 | None = None
    style: Style7 | None = None

class Attributes15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    width: int | None = None
    height: int | None = None

class HeaderItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes15 | None = None

class Attributes19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    format: str | None = None

class Style8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | None = None
    color: str | None = None

class Text1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes19 | None = None
    style: Style8 | None = None

class Attributes20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    size: int | None = None

class Icon2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes20 | None = None

class Attributes18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text1 | None = None
    icon: Icon2 | None = None
    type: str | None = None

class Style9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None

class Tag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes18 | None = None
    style: Style9 | None = None

class Attributes17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: NaiveDatetime | str | None = Field(default=None, union_mode='left_to_right')
    format: str | None = None
    number_of_lines: int | None = Field(None, alias='numberOfLines')
    tags: list[Tag] | None = None
    separator: bool | None = None

class Style10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | None = None
    color: str | None = None

class Element2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes17 | None = None
    style: Style10 | None = None

class Attributes16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    elements: list[Element2] | None = None
    type: str | None = None

class Style11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | None = None

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes16 | None = None
    style: Style11 | None = None

class ComputedRelease(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    scheduled_at: AwareDatetime | None = Field(None, alias='scheduledAt')
    computed_state: str | None = Field(None, alias='computedState')
    state: str | None = None
    type: str | None = None
    description: str | None = None

class Data5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    title: str | None = None
    access_level: str | None = Field(None, alias='accessLevel')
    online_playback: str | None = Field(None, alias='onlinePlayback')
    id: str | None = None
    computed_releases: list[ComputedRelease] | None = Field(None, alias='computedReleases')

class Action5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data5 | None = None

class Attributes14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_initial_focus: bool | None = Field(None, alias='hasInitialFocus')
    type: str | None = None
    variant: str | None = None
    header: list[HeaderItem] | None = None
    content: list[ContentItem] | None = None
    grouping_data: bool | None = Field(None, alias='groupingData')
    action: Action5 | None = None

class Card(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes14 | None = None

class Attributes12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title2 | None = None
    cards: list[Card] | None = None
    type: str | None = None

class Group(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    id: NaiveDatetime | None = None
    attributes: Attributes12 | None = None

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    elements: list[Element1] | None = None
    title: Title | None = None
    filters: list[Filter] | None = None
    actions: Actions | None = None
    groups: list[Group] | None = None

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    field_zone: str | None = Field(None, alias='$zone')
    attributes: Attributes | None = None

class ScheduleModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    layout: str | None = None
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
