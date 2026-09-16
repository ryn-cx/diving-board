from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from typing import Any
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID

class Facets(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_type: list[None] = Field(..., alias='contentType')
    genres: list[str] = Field(..., alias='Genres')
    collection_name: list[None] = Field(..., alias='collection-name')

class InitialAvailableFacets(BaseModel):
    model_config = ConfigDict(defer_build=True)
    preserve: bool
    facets: Facets

class Colors(BaseModel):
    model_config = ConfigDict(defer_build=True)
    pill_cta_default: str = Field(..., alias='pillCtaDefault')
    pill_cta_default_text: str = Field(..., alias='pillCtaDefaultText')
    pill_cta_default_border_color: str = Field(..., alias='pillCtaDefaultBorderColor')
    pill_cta_focus: str = Field(..., alias='pillCtaFocus')
    pill_cta_focus_text: str = Field(..., alias='pillCtaFocusText')
    pill_cta_focus_border_color: str = Field(..., alias='pillCtaFocusBorderColor')
    pill_cta_selected: str = Field(..., alias='pillCtaSelected')
    pill_cta_selected_text: str = Field(..., alias='pillCtaSelectedText')
    pill_cta_selected_border_color: str = Field(..., alias='pillCtaSelectedBorderColor')
    pill_cta_selected_focus: str = Field(..., alias='pillCtaSelectedFocus')
    pill_cta_selected_text_focus: str = Field(..., alias='pillCtaSelectedTextFocus')
    pill_cta_selected_border_color_focus: str = Field(..., alias='pillCtaSelectedBorderColorFocus')

class All(BaseModel):
    model_config = ConfigDict(defer_build=True)
    colors: Colors

class Theme(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all: All

class Mobile(BaseModel):
    model_config = ConfigDict(defer_build=True)
    flex_wrap: str = Field(..., alias='flexWrap')
    gap: str

class Tablet(BaseModel):
    model_config = ConfigDict(defer_build=True)
    flex_wrap: str = Field(..., alias='flexWrap')
    gap: str

class Desktop(BaseModel):
    model_config = ConfigDict(defer_build=True)
    flex_wrap: str = Field(..., alias='flexWrap')
    gap: str

class Tv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    flex_wrap: str = Field(..., alias='flexWrap')
    gap: str
    flex_shrink: int = Field(..., alias='flexShrink')
    element_width: str = Field(..., alias='elementWidth')
    margin_top: int = Field(..., alias='marginTop')

class Style(BaseModel):
    model_config = ConfigDict(defer_build=True)
    flex_wrap: str | None = Field(None, alias='flexWrap')
    margin_top: int | None = Field(None, alias='marginTop')
    mobile: Mobile | None = None
    tablet: Tablet | None = None
    desktop: Desktop | None = None
    tv: Tv | None = None

class Style1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    gap: int
    margin_top: int = Field(..., alias='marginTop')
    margin_bottom: int = Field(..., alias='marginBottom')

class Facets1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    genres: list[str] | None = Field(None, alias='Genres')

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tab: UUID | None = None
    url: str | None = None
    facets: Facets1 | None = None

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data

class Attributes2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str
    text: str
    is_selected: bool | None = Field(None, alias='isSelected')
    is_small: bool = Field(..., alias='isSmall')
    type: str
    hide_lock_icon: bool | None = Field(None, alias='hideLockIcon')
    action: Action

class Tv1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str

class Mobile1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str

class Tablet1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str

class Desktop1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str

class Style2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str | None = None
    tv: Tv1 | None = None
    mobile: Mobile1 | None = None
    tablet: Tablet1 | None = None
    desktop: Desktop1 | None = None

class Button(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes2
    style: Style2 | None = None

class Attributes3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    size: int

class AfterElement(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes3

class Data1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    facets: dict[str, Any]

class Action1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data1

class ArrowStyle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    background_color: str = Field(..., alias='backgroundColor')
    border_radius: str = Field(..., alias='borderRadius')
    border_color: str = Field(..., alias='borderColor')

class Attributes1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    style: Style1 | None = None
    is_scrollable: bool | None = Field(None, alias='isScrollable')
    buttons: list[Button] | None = None
    type: str | None = None
    accessibility_label: str | None = Field(None, alias='accessibilityLabel')
    after_element: AfterElement | None = Field(None, alias='afterElement')
    action: Action1 | None = None
    is_selected: bool | None = Field(None, alias='isSelected')
    label: str | None = None
    text: str | None = None
    is_small: bool | None = Field(None, alias='isSmall')
    is_scrollbar_hidden: bool | None = Field(None, alias='isScrollbarHidden')
    arrow_style: ArrowStyle | None = Field(None, alias='arrowStyle')

class Tv2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str | None = None
    gap: str | None = None
    padding_start: str | None = Field(None, alias='paddingStart')
    padding_end: str | None = Field(None, alias='paddingEnd')

class Style3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    align_self: str | None = Field(None, alias='alignSelf')
    flex_shrink: int | None = Field(None, alias='flexShrink')
    background_color: str | None = Field(None, alias='backgroundColor')
    border_radius: str | None = Field(None, alias='borderRadius')
    display: str | None = None
    tv: Tv2
    gap: str | None = None

class Element1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes1
    style: Style3 | None = None

class Attributes4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str | None = None
    label: str | None = None
    dynamic_label: str | None = Field(None, alias='dynamicLabel')

class Style4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color: str
    font_size: int | None = Field(None, alias='fontSize')
    line_height: str | None = Field(None, alias='lineHeight')
    size: str | None = None

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes4
    style: Style4

class Tv3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    margin_top: int = Field(..., alias='marginTop')

class Style5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    border_bottom_width: int = Field(..., alias='borderBottomWidth')
    align_self: str = Field(..., alias='alignSelf')
    tv: Tv3

class Style6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    gap: str

class Tv4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    font_weight: int | None = Field(None, alias='fontWeight')
    color: str | None = None

class Style7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size: str
    font_weight: int = Field(..., alias='fontWeight')
    tv: Tv4

class CurrentSearch(BaseModel):
    model_config = ConfigDict(defer_build=True)
    query: str
    facets_requested: str = Field(..., alias='facetsRequested')
    sort: str
    sort_direction: str = Field(..., alias='sortDirection')
    grid_view_config_id: UUID = Field(..., alias='gridViewConfigId')

class Data2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    sort: str
    sort_direction: str = Field(..., alias='sortDirection')
    current_search: CurrentSearch = Field(..., alias='currentSearch')

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data2

class Attributes6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str
    text: str
    type: str
    is_small: bool = Field(..., alias='isSmall')
    is_selected: bool | None = Field(None, alias='isSelected')
    hide_text_on_mobile: bool = Field(..., alias='hideTextOnMobile')
    action: Action2

class Button1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    field_variant: str = Field(..., alias='$variant')
    style: Style7
    attributes: Attributes6

class Attributes5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buttons: list[Button1]

class ButtonList(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    field_variant: str = Field(..., alias='$variant')
    style: Style6
    attributes: Attributes5

class Option(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    label: str
    is_visible: bool | None = Field(None, alias='isVisible')
    is_active: bool = Field(..., alias='isActive')
    value: str | None = None
    filter_key: str | None = Field(None, alias='filterKey')
    field: str | None = None
    direction: str | None = None

class Data3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Action3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data3

class Apply(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action: Action3

class CurrentSearch1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    query: str
    facets_requested: str = Field(..., alias='facetsRequested')
    sort: str
    sort_direction: str = Field(..., alias='sortDirection')
    grid_view_config_id: UUID = Field(..., alias='gridViewConfigId')
    last_seen: str = Field(..., alias='lastSeen')

class Data4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    current_search: CurrentSearch1 = Field(..., alias='currentSearch')

class Action4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data4

class Next(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    label: str
    action: Action4

class Actions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    apply: Apply | None = None
    next: Next | None = None

class CurrentSearch2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    query: str
    facets_requested: str = Field(..., alias='facetsRequested')
    sort: str
    sort_direction: str = Field(..., alias='sortDirection')
    grid_view_config_id: UUID = Field(..., alias='gridViewConfigId')

class Data5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    current_search: CurrentSearch2 = Field(..., alias='currentSearch')

class Action5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data5

class Desktop2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size_type: str = Field(..., alias='sizeType')

class Tv5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size_type: str = Field(..., alias='sizeType')

class Tablet2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size_type: str = Field(..., alias='sizeType')

class Mobile2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size_type: str = Field(..., alias='sizeType')

class Breakpoints(BaseModel):
    model_config = ConfigDict(defer_build=True)
    desktop: Desktop2
    tv: Tv5
    tablet: Tablet2
    mobile: Mobile2

class Style8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    auto_width: bool = Field(..., alias='autoWidth')
    border_radius: int = Field(..., alias='borderRadius')

class Attributes8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str | None = None
    border_radius: int = Field(..., alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes8

class Tv6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    gap: int

class Breakpoints2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tv: Tv6

class Style9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    element_padding_top: str = Field(..., alias='elementPaddingTop')
    gap: str

class Attributes10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    number_of_lines: int = Field(..., alias='numberOfLines')

class Tablet3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    font_size: int = Field(..., alias='fontSize')

class Mobile3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    font_size: int = Field(..., alias='fontSize')

class Style10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color: str
    size: str
    tablet: Tablet3
    mobile: Mobile3

class Element2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes10
    style: Style10

class Attributes9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    align: str
    type: str
    gap: int
    breakpoints: Breakpoints2
    element_padding_top: int = Field(..., alias='elementPaddingTop')
    style: Style9
    elements: list[Element2]

class ContentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes9

class Desktop3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size_type: str = Field(..., alias='sizeType')
    header: list[HeaderItem]
    content: list[ContentItem]

class Attributes11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str | None = None
    border_radius: int = Field(..., alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes11

class Breakpoints3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tv: Tv6

class Style11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    element_padding_top: str = Field(..., alias='elementPaddingTop')
    gap: str

class Attributes13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    number_of_lines: int = Field(..., alias='numberOfLines')

class Style12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color: str
    size: str
    tablet: Tablet3
    mobile: Mobile3

class Element3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes13
    style: Style12

class Attributes12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    align: str
    type: str
    gap: int
    breakpoints: Breakpoints3
    element_padding_top: int = Field(..., alias='elementPaddingTop')
    style: Style11
    elements: list[Element3]

class ContentItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes12

class Tv7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size_type: str = Field(..., alias='sizeType')
    header: list[HeaderItem1]
    content: list[ContentItem1]

class Attributes14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str | None = None
    border_radius: int = Field(..., alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes14

class Tv9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    gap: int

class Breakpoints4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tv: Tv9

class Style13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    element_padding_top: str = Field(..., alias='elementPaddingTop')
    gap: str

class Attributes16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    number_of_lines: int = Field(..., alias='numberOfLines')

class Style14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color: str
    size: str
    tablet: Tablet3
    mobile: Mobile3

class Element4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes16
    style: Style14

class Attributes15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    align: str
    type: str
    gap: int
    breakpoints: Breakpoints4
    element_padding_top: int = Field(..., alias='elementPaddingTop')
    style: Style13
    elements: list[Element4]

class ContentItem2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes15

class Tablet5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size_type: str = Field(..., alias='sizeType')
    header: list[HeaderItem2]
    content: list[ContentItem2]

class Attributes17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str | None = None
    border_radius: int = Field(..., alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes17

class Breakpoints5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tv: Tv9

class Style15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    element_padding_top: str = Field(..., alias='elementPaddingTop')
    gap: str

class Attributes19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    number_of_lines: int = Field(..., alias='numberOfLines')

class Tablet7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    font_size: int = Field(..., alias='fontSize')

class Style16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color: str
    size: str
    tablet: Tablet7
    mobile: Mobile3

class Element5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes19
    style: Style16

class Attributes18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    align: str
    type: str
    gap: int
    breakpoints: Breakpoints5
    element_padding_top: int = Field(..., alias='elementPaddingTop')
    style: Style15
    elements: list[Element5]

class ContentItem3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes18

class Mobile6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size_type: str = Field(..., alias='sizeType')
    header: list[HeaderItem3]
    content: list[ContentItem3]

class Breakpoints1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    desktop: Desktop3
    tv: Tv7
    tablet: Tablet5
    mobile: Mobile6

class ContentStyle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    margin_top: int = Field(..., alias='marginTop')

class Attributes20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str | None = None
    width: int | None = None
    height: int | None = None
    border_radius: int = Field(..., alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes20

class ComputedRelease(BaseModel):
    model_config = ConfigDict(defer_build=True)
    scheduled_at: AwareDatetime = Field(..., alias='scheduledAt')
    computed_state: str = Field(..., alias='computedState')
    state: str
    type: str
    description: str

class Data6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    title: str
    access_level: str = Field(..., alias='accessLevel')
    id: str
    computed_releases: list[ComputedRelease] = Field(..., alias='computedReleases')

class Action6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data6

class Attributes7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid_version: int = Field(..., alias='gridVersion')
    style: Style8
    breakpoints: Breakpoints1
    type: str
    has_initial_focus: bool = Field(..., alias='hasInitialFocus')
    content_style: ContentStyle = Field(..., alias='contentStyle')
    header: list[HeaderItem4]
    action: Action6

class Card(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes7

class Attributes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str | None = None
    elements: list[Element1] | None = None
    disable_filter_column_tv: bool | None = Field(None, alias='disableFilterColumnTv')
    align: str | None = None
    title: Title | None = None
    style: Style5 | None = None
    button_list: ButtonList | None = Field(None, alias='buttonList')
    filters: list[None] | None = None
    options: list[Option] | None = None
    actions: Actions | None = None
    action: Action5 | None = None
    disable_force_focus: bool | None = Field(None, alias='disableForceFocus')
    grid_version: int | None = Field(None, alias='gridVersion')
    breakpoints: Breakpoints | None = None
    cards: list[Card] | None = None

class Element(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_zone: str = Field(..., alias='$zone')
    field_type: str = Field(..., alias='$type')
    style: Style | None = None
    attributes: Attributes
    field_variant: str | None = Field(None, alias='$variant')

class ContentGridModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    initial_available_facets: InitialAvailableFacets = Field(..., alias='initialAvailableFacets')
    theme: Theme
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
