from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, NaiveDatetime

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    size: int | Any = Field(default=None, union_mode='left_to_right')

class Icon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes3 | Any = Field(default=None, union_mode='left_to_right')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    from_: NaiveDatetime | Any = Field(None, alias='from', union_mode='left_to_right')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data | Any = Field(default=None, union_mode='left_to_right')

class Attributes2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon | Any = Field(default=None, union_mode='left_to_right')
    action: Action | Any = Field(default=None, union_mode='left_to_right')

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | Any = Field(default=None, union_mode='left_to_right')

class Forward(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes2 | Any = Field(default=None, union_mode='left_to_right')
    style: Style | Any = Field(default=None, union_mode='left_to_right')

class Attributes5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    size: int | Any = Field(default=None, union_mode='left_to_right')

class Icon1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes5 | Any = Field(default=None, union_mode='left_to_right')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data | Any = Field(default=None, union_mode='left_to_right')

class Attributes4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon1 | Any = Field(default=None, union_mode='left_to_right')
    action: Action1 | Any = Field(default=None, union_mode='left_to_right')

class Back(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes4 | Any = Field(default=None, union_mode='left_to_right')
    style: Style | Any = Field(default=None, union_mode='left_to_right')

class Attributes6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    format: str | Any = Field(default=None, union_mode='left_to_right')

class Style2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | Any = Field(default=None, union_mode='left_to_right')
    size: float | Any = Field(default=None, union_mode='left_to_right')

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes6 | Any = Field(default=None, union_mode='left_to_right')
    style: Style2 | Any = Field(default=None, union_mode='left_to_right')

class Attributes8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    size: int | Any = Field(default=None, union_mode='left_to_right')

class AfterElement(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes8 | Any = Field(default=None, union_mode='left_to_right')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    is_small: bool | Any = Field(None, alias='isSmall', union_mode='left_to_right')
    after_element: AfterElement | Any = Field(None, alias='afterElement', union_mode='left_to_right')
    action: Action2 | Any = Field(default=None, union_mode='left_to_right')

class Style3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: float | Any = Field(default=None, union_mode='left_to_right')

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes7 | Any = Field(default=None, union_mode='left_to_right')
    style: Style3 | Any = Field(default=None, union_mode='left_to_right')

class Attributes1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    forward: Forward | Any = Field(default=None, union_mode='left_to_right')
    back: Back | Any = Field(default=None, union_mode='left_to_right')
    text: Text | Any = Field(default=None, union_mode='left_to_right')
    buttons: list[Button] | Any = Field(default=None, union_mode='left_to_right')

class Style4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Element1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes1 | Any = Field(default=None, union_mode='left_to_right')
    style: Style4 | Any = Field(default=None, union_mode='left_to_right')

class Attributes9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Style5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: int | Any = Field(default=None, union_mode='left_to_right')
    color: str | Any = Field(default=None, union_mode='left_to_right')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes9 | Any = Field(default=None, union_mode='left_to_right')
    style: Style5 | Any = Field(default=None, union_mode='left_to_right')

class Attributes11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')
    number_of_lines: int | Any = Field(None, alias='numberOfLines', union_mode='left_to_right')

class Style6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | Any = Field(default=None, union_mode='left_to_right')
    color: str | Any = Field(default=None, union_mode='left_to_right')

class Title1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes11 | Any = Field(default=None, union_mode='left_to_right')
    style: Style6 | Any = Field(default=None, union_mode='left_to_right')

class Option(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    filter_key: str | Any = Field(None, alias='filterKey', union_mode='left_to_right')
    is_active: bool | Any = Field(None, alias='isActive', union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    format: str | Any = Field(default=None, union_mode='left_to_right')
    value: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title1 | Any = Field(default=None, union_mode='left_to_right')
    filter_key: str | Any = Field(None, alias='filterKey', union_mode='left_to_right')
    options: list[Option] | Any = Field(default=None, union_mode='left_to_right')

class Filter(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes10 | Any = Field(default=None, union_mode='left_to_right')

class Data2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data2 | Any = Field(default=None, union_mode='left_to_right')

class Reset(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action3 | Any = Field(default=None, union_mode='left_to_right')

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data2 | Any = Field(default=None, union_mode='left_to_right')

class Apply(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action4 | Any = Field(default=None, union_mode='left_to_right')

class Data4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    last_seen: str | Any = Field(None, alias='lastSeen', union_mode='left_to_right')

class Next(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data4 | Any = Field(default=None, union_mode='left_to_right')

class Actions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    reset: Reset | Any = Field(default=None, union_mode='left_to_right')
    apply: Apply | Any = Field(default=None, union_mode='left_to_right')
    next: Next | Any = Field(default=None, union_mode='left_to_right')

class Attributes13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: NaiveDatetime | Any = Field(default=None, union_mode='left_to_right')
    format: str | Any = Field(default=None, union_mode='left_to_right')

class Style7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | Any = Field(default=None, union_mode='left_to_right')
    size: float | Any = Field(default=None, union_mode='left_to_right')

class Title2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes13 | Any = Field(default=None, union_mode='left_to_right')
    style: Style7 | Any = Field(default=None, union_mode='left_to_right')

class Attributes15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class HeaderItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes15 | Any = Field(default=None, union_mode='left_to_right')

class Attributes19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    format: str | Any = Field(default=None, union_mode='left_to_right')

class Style8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | Any = Field(default=None, union_mode='left_to_right')
    color: str | Any = Field(default=None, union_mode='left_to_right')

class Text1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes19 | Any = Field(default=None, union_mode='left_to_right')
    style: Style8 | Any = Field(default=None, union_mode='left_to_right')

class Attributes20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    size: int | Any = Field(default=None, union_mode='left_to_right')

class Icon2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes20 | Any = Field(default=None, union_mode='left_to_right')

class Attributes18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text1 | Any = Field(default=None, union_mode='left_to_right')
    icon: Icon2 | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Style9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | Any = Field(default=None, union_mode='left_to_right')

class Tag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes18 | Any = Field(default=None, union_mode='left_to_right')
    style: Style9 | Any = Field(default=None, union_mode='left_to_right')

class Attributes17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: NaiveDatetime | str | Any = Field(default=None, union_mode='left_to_right')
    format: str | Any = Field(default=None, union_mode='left_to_right')
    number_of_lines: int | Any = Field(None, alias='numberOfLines', union_mode='left_to_right')
    tags: list[Tag] | Any = Field(default=None, union_mode='left_to_right')
    separator: bool | Any = Field(default=None, union_mode='left_to_right')

class Style10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | Any = Field(default=None, union_mode='left_to_right')
    color: str | Any = Field(default=None, union_mode='left_to_right')

class Element2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes17 | Any = Field(default=None, union_mode='left_to_right')
    style: Style10 | Any = Field(default=None, union_mode='left_to_right')

class Attributes16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    elements: list[Element2] | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Style11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | Any = Field(default=None, union_mode='left_to_right')

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes16 | Any = Field(default=None, union_mode='left_to_right')
    style: Style11 | Any = Field(default=None, union_mode='left_to_right')

class ComputedRelease(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    scheduled_at: AwareDatetime | Any = Field(None, alias='scheduledAt', union_mode='left_to_right')
    computed_state: str | Any = Field(None, alias='computedState', union_mode='left_to_right')
    state: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Data5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')
    online_playback: str | Any = Field(None, alias='onlinePlayback', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    computed_releases: list[ComputedRelease] | Any = Field(None, alias='computedReleases', union_mode='left_to_right')

class Action5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data5 | Any = Field(default=None, union_mode='left_to_right')

class Attributes14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_initial_focus: bool | Any = Field(None, alias='hasInitialFocus', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    variant: str | Any = Field(default=None, union_mode='left_to_right')
    header: list[HeaderItem] | Any = Field(default=None, union_mode='left_to_right')
    content: list[ContentItem] | Any = Field(default=None, union_mode='left_to_right')
    grouping_data: bool | Any = Field(None, alias='groupingData', union_mode='left_to_right')
    action: Action5 | Any = Field(default=None, union_mode='left_to_right')

class Card(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes14 | Any = Field(default=None, union_mode='left_to_right')

class Attributes12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title2 | Any = Field(default=None, union_mode='left_to_right')
    cards: list[Card] | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Group(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    id: NaiveDatetime | Any = Field(default=None, union_mode='left_to_right')
    attributes: Attributes12 | Any = Field(default=None, union_mode='left_to_right')

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    elements: list[Element1] | Any = Field(default=None, union_mode='left_to_right')
    title: Title | Any = Field(default=None, union_mode='left_to_right')
    filters: list[Filter] | Any = Field(default=None, union_mode='left_to_right')
    actions: Actions | Any = Field(default=None, union_mode='left_to_right')
    groups: list[Group] | Any = Field(default=None, union_mode='left_to_right')

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    field_zone: str | Any = Field(None, alias='$zone', union_mode='left_to_right')
    attributes: Attributes | Any = Field(default=None, union_mode='left_to_right')

class ScheduleModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    layout: str | Any = Field(default=None, union_mode='left_to_right')
    elements: list[Element] | Any = Field(default=None, union_mode='left_to_right')
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
