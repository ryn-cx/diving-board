from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID

class Facets(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_type: list[Any] | None = Field(None, alias='contentType')
    genres: list[str] | None = Field(None, alias='Genres')
    collection_name: list[Any] | None = Field(None, alias='collection-name')

class InitialAvailableFacets(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    preserve: bool | None = None
    facets: Facets | None = None

class Colors(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    pill_cta_default: str | None = Field(None, alias='pillCtaDefault')
    pill_cta_default_text: str | None = Field(None, alias='pillCtaDefaultText')
    pill_cta_default_border_color: str | None = Field(None, alias='pillCtaDefaultBorderColor')
    pill_cta_focus: str | None = Field(None, alias='pillCtaFocus')
    pill_cta_focus_text: str | None = Field(None, alias='pillCtaFocusText')
    pill_cta_focus_border_color: str | None = Field(None, alias='pillCtaFocusBorderColor')
    pill_cta_selected: str | None = Field(None, alias='pillCtaSelected')
    pill_cta_selected_text: str | None = Field(None, alias='pillCtaSelectedText')
    pill_cta_selected_border_color: str | None = Field(None, alias='pillCtaSelectedBorderColor')
    pill_cta_selected_focus: str | None = Field(None, alias='pillCtaSelectedFocus')
    pill_cta_selected_text_focus: str | None = Field(None, alias='pillCtaSelectedTextFocus')
    pill_cta_selected_border_color_focus: str | None = Field(None, alias='pillCtaSelectedBorderColorFocus')

class All(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    colors: Colors | None = None

class Theme(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    all: All | None = None

class Mobile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | None = Field(None, alias='flexWrap')
    gap: str | None = None

class Tablet(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | None = Field(None, alias='flexWrap')
    gap: str | None = None

class Desktop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | None = Field(None, alias='flexWrap')
    gap: str | None = None

class Tv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | None = Field(None, alias='flexWrap')
    gap: str | None = None
    flex_shrink: int | None = Field(None, alias='flexShrink')
    element_width: str | None = Field(None, alias='elementWidth')
    margin_top: int | None = Field(None, alias='marginTop')

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | None = Field(None, alias='flexWrap')
    margin_top: int | None = Field(None, alias='marginTop')
    mobile: Mobile | None = None
    tablet: Tablet | None = None
    desktop: Desktop | None = None
    tv: Tv | None = None

class Style1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: int | None = None
    margin_top: int | None = Field(None, alias='marginTop')
    margin_bottom: int | None = Field(None, alias='marginBottom')

class Facets1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genres: list[str] | None = Field(None, alias='Genres')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tab: UUID | None = None
    url: str | None = None
    facets: Facets1 | None = None

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data | None = None

class Attributes2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None
    text: str | None = None
    is_selected: bool | None = Field(None, alias='isSelected')
    is_small: bool | None = Field(None, alias='isSmall')
    type: str | None = None
    hide_lock_icon: bool | None = Field(None, alias='hideLockIcon')
    action: Action | None = None

class Tv1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | None = None

class Mobile1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | None = None

class Tablet1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | None = None

class Desktop1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | None = None

class Style2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | None = None
    tv: Tv1 | None = None
    mobile: Mobile1 | None = None
    tablet: Tablet1 | None = None
    desktop: Desktop1 | None = None

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes2 | None = None
    style: Style2 | None = None

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    size: int | None = None

class AfterElement(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes3 | None = None

class Data1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    facets: dict[str, Any] | None = None

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data1 | None = None

class ArrowStyle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    background_color: str | None = Field(None, alias='backgroundColor')
    border_radius: str | None = Field(None, alias='borderRadius')
    border_color: str | None = Field(None, alias='borderColor')

class Attributes1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
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
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | None = None
    gap: str | None = None
    padding_start: str | None = Field(None, alias='paddingStart')
    padding_end: str | None = Field(None, alias='paddingEnd')

class Style3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align_self: str | None = Field(None, alias='alignSelf')
    flex_shrink: int | None = Field(None, alias='flexShrink')
    background_color: str | None = Field(None, alias='backgroundColor')
    border_radius: str | None = Field(None, alias='borderRadius')
    display: str | None = None
    tv: Tv2 | None = None
    gap: str | None = None

class Element1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes1 | None = None
    style: Style3 | None = None

class Attributes4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    label: str | None = None
    dynamic_label: str | None = Field(None, alias='dynamicLabel')

class Style4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None
    font_size: int | None = Field(None, alias='fontSize')
    line_height: str | None = Field(None, alias='lineHeight')
    size: str | None = None

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes4 | None = None
    style: Style4 | None = None

class Tv3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    margin_top: int | None = Field(None, alias='marginTop')

class Style5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    border_bottom_width: int | None = Field(None, alias='borderBottomWidth')
    align_self: str | None = Field(None, alias='alignSelf')
    tv: Tv3 | None = None

class Style6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: str | None = None

class Tv4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    font_weight: int | None = Field(None, alias='fontWeight')
    color: str | None = None

class Style7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | None = None
    font_weight: int | None = Field(None, alias='fontWeight')
    tv: Tv4 | None = None

class CurrentSearch(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | None = None
    facets_requested: str | None = Field(None, alias='facetsRequested')
    sort: str | None = None
    sort_direction: str | None = Field(None, alias='sortDirection')
    grid_view_config_id: UUID | None = Field(None, alias='gridViewConfigId')

class Data2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    sort: str | None = None
    sort_direction: str | None = Field(None, alias='sortDirection')
    current_search: CurrentSearch | None = Field(None, alias='currentSearch')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data2 | None = None

class Attributes6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None
    text: str | None = None
    type: str | None = None
    is_small: bool | None = Field(None, alias='isSmall')
    is_selected: bool | None = Field(None, alias='isSelected')
    hide_text_on_mobile: bool | None = Field(None, alias='hideTextOnMobile')
    action: Action2 | None = None

class Button1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    field_variant: str | None = Field(None, alias='$variant')
    style: Style7 | None = None
    attributes: Attributes6 | None = None

class Attributes5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    buttons: list[Button1] | None = None

class ButtonList(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    field_variant: str | None = Field(None, alias='$variant')
    style: Style6 | None = None
    attributes: Attributes5 | None = None

class Option(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    label: str | None = None
    is_visible: bool | None = Field(None, alias='isVisible')
    is_active: bool | None = Field(None, alias='isActive')
    value: str | None = None
    filter_key: str | None = Field(None, alias='filterKey')
    field: str | None = None
    direction: str | None = None

class Data3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data3 | None = None

class Apply(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action: Action3 | None = None

class CurrentSearch1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | None = None
    facets_requested: str | None = Field(None, alias='facetsRequested')
    sort: str | None = None
    sort_direction: str | None = Field(None, alias='sortDirection')
    grid_view_config_id: UUID | None = Field(None, alias='gridViewConfigId')
    last_seen: str | None = Field(None, alias='lastSeen')

class Data4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    current_search: CurrentSearch1 | None = Field(None, alias='currentSearch')

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data4 | None = None

class Next(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    label: str | None = None
    action: Action4 | None = None

class Actions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    apply: Apply | None = None
    next: Next | None = None

class CurrentSearch2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | None = None
    facets_requested: str | None = Field(None, alias='facetsRequested')
    sort: str | None = None
    sort_direction: str | None = Field(None, alias='sortDirection')
    grid_view_config_id: UUID | None = Field(None, alias='gridViewConfigId')

class Data5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    current_search: CurrentSearch2 | None = Field(None, alias='currentSearch')

class Action5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data5 | None = None

class Desktop2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | None = Field(None, alias='sizeType')

class Tv5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | None = Field(None, alias='sizeType')

class Tablet2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | None = Field(None, alias='sizeType')

class Mobile2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | None = Field(None, alias='sizeType')

class Breakpoints(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop: Desktop2 | None = None
    tv: Tv5 | None = None
    tablet: Tablet2 | None = None
    mobile: Mobile2 | None = None

class Style8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    auto_width: bool | None = Field(None, alias='autoWidth')
    border_radius: int | None = Field(None, alias='borderRadius')

class Attributes8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    border_radius: int | None = Field(None, alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes8 | None = None

class Tv6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: int | None = None

class Breakpoints2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tv: Tv6 | None = None

class Style9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    element_padding_top: str | None = Field(None, alias='elementPaddingTop')
    gap: str | None = None

class Attributes10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    number_of_lines: int | None = Field(None, alias='numberOfLines')

class Tablet3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    font_size: int | None = Field(None, alias='fontSize')

class Mobile3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    font_size: int | None = Field(None, alias='fontSize')

class Style10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None
    size: str | None = None
    tablet: Tablet3 | None = None
    mobile: Mobile3 | None = None

class Element2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes10 | None = None
    style: Style10 | None = None

class Attributes9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | None = None
    type: str | None = None
    gap: int | None = None
    breakpoints: Breakpoints2 | None = None
    element_padding_top: int | None = Field(None, alias='elementPaddingTop')
    style: Style9 | None = None
    elements: list[Element2] | None = None

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes9 | None = None

class Desktop3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | None = Field(None, alias='sizeType')
    header: list[HeaderItem] | None = None
    content: list[ContentItem] | None = None

class Attributes11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    border_radius: int | None = Field(None, alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes11 | None = None

class Breakpoints3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tv: Tv6 | None = None

class Style11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    element_padding_top: str | None = Field(None, alias='elementPaddingTop')
    gap: str | None = None

class Attributes13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    number_of_lines: int | None = Field(None, alias='numberOfLines')

class Style12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None
    size: str | None = None
    tablet: Tablet3 | None = None
    mobile: Mobile3 | None = None

class Element3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes13 | None = None
    style: Style12 | None = None

class Attributes12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | None = None
    type: str | None = None
    gap: int | None = None
    breakpoints: Breakpoints3 | None = None
    element_padding_top: int | None = Field(None, alias='elementPaddingTop')
    style: Style11 | None = None
    elements: list[Element3] | None = None

class ContentItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes12 | None = None

class Tv7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | None = Field(None, alias='sizeType')
    header: list[HeaderItem1] | None = None
    content: list[ContentItem1] | None = None

class Attributes14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    border_radius: int | None = Field(None, alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes14 | None = None

class Tv9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: int | None = None

class Breakpoints4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tv: Tv9 | None = None

class Style13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    element_padding_top: str | None = Field(None, alias='elementPaddingTop')
    gap: str | None = None

class Attributes16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    number_of_lines: int | None = Field(None, alias='numberOfLines')

class Style14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None
    size: str | None = None
    tablet: Tablet3 | None = None
    mobile: Mobile3 | None = None

class Element4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes16 | None = None
    style: Style14 | None = None

class Attributes15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | None = None
    type: str | None = None
    gap: int | None = None
    breakpoints: Breakpoints4 | None = None
    element_padding_top: int | None = Field(None, alias='elementPaddingTop')
    style: Style13 | None = None
    elements: list[Element4] | None = None

class ContentItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes15 | None = None

class Tablet5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | None = Field(None, alias='sizeType')
    header: list[HeaderItem2] | None = None
    content: list[ContentItem2] | None = None

class Attributes17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    border_radius: int | None = Field(None, alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes17 | None = None

class Breakpoints5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tv: Tv9 | None = None

class Style15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    element_padding_top: str | None = Field(None, alias='elementPaddingTop')
    gap: str | None = None

class Attributes19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    number_of_lines: int | None = Field(None, alias='numberOfLines')

class Tablet7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    font_size: int | None = Field(None, alias='fontSize')

class Style16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None
    size: str | None = None
    tablet: Tablet7 | None = None
    mobile: Mobile3 | None = None

class Element5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes19 | None = None
    style: Style16 | None = None

class Attributes18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | None = None
    type: str | None = None
    gap: int | None = None
    breakpoints: Breakpoints5 | None = None
    element_padding_top: int | None = Field(None, alias='elementPaddingTop')
    style: Style15 | None = None
    elements: list[Element5] | None = None

class ContentItem3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes18 | None = None

class Mobile6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | None = Field(None, alias='sizeType')
    header: list[HeaderItem3] | None = None
    content: list[ContentItem3] | None = None

class Breakpoints1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop: Desktop3 | None = None
    tv: Tv7 | None = None
    tablet: Tablet5 | None = None
    mobile: Mobile6 | None = None

class ContentStyle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    margin_top: int | None = Field(None, alias='marginTop')

class Attributes20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    width: int | None = None
    height: int | None = None
    border_radius: int | None = Field(None, alias='borderRadius')
    access_level: str | None = Field(None, alias='accessLevel')

class HeaderItem4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes20 | None = None

class ComputedRelease(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    scheduled_at: AwareDatetime | None = Field(None, alias='scheduledAt')
    computed_state: str | None = Field(None, alias='computedState')
    state: str | None = None
    type: str | None = None
    description: str | None = None

class Data6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    title: str | None = None
    access_level: str | None = Field(None, alias='accessLevel')
    id: str | None = None
    computed_releases: list[ComputedRelease] | None = Field(None, alias='computedReleases')

class Action6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data6 | None = None

class Attributes7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid_version: int | None = Field(None, alias='gridVersion')
    style: Style8 | None = None
    breakpoints: Breakpoints1 | None = None
    type: str | None = None
    has_initial_focus: bool | None = Field(None, alias='hasInitialFocus')
    content_style: ContentStyle | None = Field(None, alias='contentStyle')
    header: list[HeaderItem4] | None = None
    action: Action6 | None = None

class Card(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes7 | None = None

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    elements: list[Element1] | None = None
    disable_filter_column_tv: bool | None = Field(None, alias='disableFilterColumnTv')
    align: str | None = None
    title: Title | None = None
    style: Style5 | None = None
    button_list: ButtonList | None = Field(None, alias='buttonList')
    filters: list[Any] | None = None
    options: list[Option] | None = None
    actions: Actions | None = None
    action: Action5 | None = None
    disable_force_focus: bool | None = Field(None, alias='disableForceFocus')
    grid_version: int | None = Field(None, alias='gridVersion')
    breakpoints: Breakpoints | None = None
    cards: list[Card] | None = None

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_zone: str | None = Field(None, alias='$zone')
    field_type: str | None = Field(None, alias='$type')
    style: Style | None = None
    attributes: Attributes | None = None
    field_variant: str | None = Field(None, alias='$variant')

class ContentGridModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    initial_available_facets: InitialAvailableFacets | None = Field(None, alias='initialAvailableFacets')
    theme: Theme | None = None
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
