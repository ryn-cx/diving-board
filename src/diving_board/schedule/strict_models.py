from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field

class Attributes3(BaseModel):
    icon: str
    size: int

class Icon(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes3

class Data(BaseModel):
    from_: AwareDatetime = Field(..., alias='from')

class Action(BaseModel):
    type: str
    data: Data

class Attributes2(BaseModel):
    type: str
    icon: Icon
    action: Action

class Style(BaseModel):
    size: str

class Forward(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes2
    style: Style

class Attributes5(BaseModel):
    icon: str
    size: int

class Icon1(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes5

class Action1(BaseModel):
    type: str
    data: Data

class Attributes4(BaseModel):
    type: str
    icon: Icon1
    action: Action1

class Back(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes4
    style: Style

class Attributes6(BaseModel):
    text: str
    format: str

class Style2(BaseModel):
    color: str
    size: float

class Text(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes6
    style: Style2

class Attributes8(BaseModel):
    icon: str
    size: int

class AfterElement(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes8

class Action2(BaseModel):
    type: str

class Attributes7(BaseModel):
    text: str
    label: str
    type: str
    is_small: bool = Field(..., alias='isSmall')
    after_element: AfterElement = Field(..., alias='afterElement')
    action: Action2

class Style3(BaseModel):
    size: float

class Button(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes7
    style: Style3

class Attributes1(BaseModel):
    forward: Forward | None = None
    back: Back | None = None
    text: Text | None = None
    buttons: list[Button] | None = None

class Style4(BaseModel):
    gap: str

class Element1(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes1
    style: Style4 | None = None

class Attributes9(BaseModel):
    text: str
    label: str

class Style5(BaseModel):
    size: int
    color: str

class Title(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes9
    style: Style5

class Attributes11(BaseModel):
    label: str
    number_of_lines: int = Field(..., alias='numberOfLines')

class Style6(BaseModel):
    size: str
    color: str

class Title1(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes11
    style: Style6

class Option(BaseModel):
    type: str
    filter_key: str = Field(..., alias='filterKey')
    is_active: bool = Field(..., alias='isActive')
    text: str
    format: str
    value: str

class Attributes10(BaseModel):
    title: Title1
    filter_key: str = Field(..., alias='filterKey')
    options: list[Option]

class Filter(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes10

class Data2(BaseModel):
    url: str

class Action3(BaseModel):
    type: str
    data: Data2

class Reset(BaseModel):
    label: str
    text: str
    action: Action3

class Action4(BaseModel):
    type: str
    data: Data2

class Apply(BaseModel):
    label: str
    text: str
    action: Action4

class Data4(BaseModel):
    last_seen: str = Field(..., alias='lastSeen')

class Next(BaseModel):
    type: str
    data: Data4

class Actions(BaseModel):
    reset: Reset | None = None
    apply: Apply | None = None
    next: Next | None = None

class Attributes13(BaseModel):
    text: AwareDatetime
    format: str

class Style7(BaseModel):
    color: str
    size: float

class Title2(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes13
    style: Style7

class Attributes15(BaseModel):
    source: str
    width: int
    height: int

class HeaderItem(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes15

class Attributes19(BaseModel):
    text: str
    format: str | None = None

class Style8(BaseModel):
    size: str
    color: str | None = None

class Text1(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes19
    style: Style8

class Attributes20(BaseModel):
    icon: str
    size: int

class Icon2(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes20

class Attributes18(BaseModel):
    text: Text1
    icon: Icon2 | None = None
    type: str

class Style9(BaseModel):
    color: str

class Tag(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes18 | None = None
    style: Style9 | None = None

class Attributes17(BaseModel):
    text: AwareDatetime | str | None = Field(default=None, union_mode='left_to_right')
    format: str | None = None
    number_of_lines: int | None = Field(None, alias='numberOfLines')
    tags: list[Tag] | None = None
    separator: bool | None = None

class Style10(BaseModel):
    size: str
    color: str

class Element2(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes17
    style: Style10 | None = None

class Attributes16(BaseModel):
    elements: list[Element2]
    type: str

class Style11(BaseModel):
    align: str

class ContentItem(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes16
    style: Style11

class ComputedRelease(BaseModel):
    scheduled_at: AwareDatetime = Field(..., alias='scheduledAt')
    computed_state: str = Field(..., alias='computedState')
    state: str
    type: str
    description: str

class Data5(BaseModel):
    type: str
    title: str
    access_level: str = Field(..., alias='accessLevel')
    online_playback: str = Field(..., alias='onlinePlayback')
    id: str
    computed_releases: list[ComputedRelease] = Field(..., alias='computedReleases')

class Action5(BaseModel):
    type: str
    data: Data5

class Attributes14(BaseModel):
    has_initial_focus: bool = Field(..., alias='hasInitialFocus')
    type: str
    variant: str
    header: list[HeaderItem]
    content: list[ContentItem]
    grouping_data: bool = Field(..., alias='groupingData')
    action: Action5

class Card(BaseModel):
    field_type: str = Field(..., alias='$type')
    attributes: Attributes14

class Attributes12(BaseModel):
    title: Title2
    cards: list[Card]
    type: str

class Group(BaseModel):
    field_type: str = Field(..., alias='$type')
    id: AwareDatetime
    attributes: Attributes12

class Attributes(BaseModel):
    elements: list[Element1] | None = None
    title: Title | None = None
    filters: list[Filter] | None = None
    actions: Actions | None = None
    groups: list[Group] | None = None

class Element(BaseModel):
    field_type: str = Field(..., alias='$type')
    field_zone: str = Field(..., alias='$zone')
    attributes: Attributes

class ScheduleModel(BaseModel):
    layout: str
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
