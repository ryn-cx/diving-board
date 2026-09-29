from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID

class Facets(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_type: list[Any] | Any = Field(None, alias='contentType', union_mode='left_to_right')
    genres: list[str] | Any = Field(None, alias='Genres', union_mode='left_to_right')
    collection_name: list[Any] | Any = Field(None, alias='collection-name', union_mode='left_to_right')

class InitialAvailableFacets(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    preserve: bool | Any = Field(default=None, union_mode='left_to_right')
    facets: Facets | Any = Field(default=None, union_mode='left_to_right')

class Colors(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    pill_cta_default: str | Any = Field(None, alias='pillCtaDefault', union_mode='left_to_right')
    pill_cta_default_text: str | Any = Field(None, alias='pillCtaDefaultText', union_mode='left_to_right')
    pill_cta_default_border_color: str | Any = Field(None, alias='pillCtaDefaultBorderColor', union_mode='left_to_right')
    pill_cta_focus: str | Any = Field(None, alias='pillCtaFocus', union_mode='left_to_right')
    pill_cta_focus_text: str | Any = Field(None, alias='pillCtaFocusText', union_mode='left_to_right')
    pill_cta_focus_border_color: str | Any = Field(None, alias='pillCtaFocusBorderColor', union_mode='left_to_right')
    pill_cta_selected: str | Any = Field(None, alias='pillCtaSelected', union_mode='left_to_right')
    pill_cta_selected_text: str | Any = Field(None, alias='pillCtaSelectedText', union_mode='left_to_right')
    pill_cta_selected_border_color: str | Any = Field(None, alias='pillCtaSelectedBorderColor', union_mode='left_to_right')
    pill_cta_selected_focus: str | Any = Field(None, alias='pillCtaSelectedFocus', union_mode='left_to_right')
    pill_cta_selected_text_focus: str | Any = Field(None, alias='pillCtaSelectedTextFocus', union_mode='left_to_right')
    pill_cta_selected_border_color_focus: str | Any = Field(None, alias='pillCtaSelectedBorderColorFocus', union_mode='left_to_right')

class All(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    colors: Colors | Any = Field(default=None, union_mode='left_to_right')

class Theme(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    all: All | Any = Field(default=None, union_mode='left_to_right')

class Mobile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | Any = Field(None, alias='flexWrap', union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Tablet(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | Any = Field(None, alias='flexWrap', union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Desktop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | Any = Field(None, alias='flexWrap', union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Tv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | Any = Field(None, alias='flexWrap', union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')
    flex_shrink: int | Any = Field(None, alias='flexShrink', union_mode='left_to_right')
    element_width: str | Any = Field(None, alias='elementWidth', union_mode='left_to_right')
    margin_top: int | Any = Field(None, alias='marginTop', union_mode='left_to_right')

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    flex_wrap: str | Any = Field(None, alias='flexWrap', union_mode='left_to_right')
    margin_top: int | Any = Field(None, alias='marginTop', union_mode='left_to_right')
    mobile: Mobile | Any = Field(default=None, union_mode='left_to_right')
    tablet: Tablet | Any = Field(default=None, union_mode='left_to_right')
    desktop: Desktop | Any = Field(default=None, union_mode='left_to_right')
    tv: Tv | Any = Field(default=None, union_mode='left_to_right')

class Style1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: int | Any = Field(default=None, union_mode='left_to_right')
    margin_top: int | Any = Field(None, alias='marginTop', union_mode='left_to_right')
    margin_bottom: int | Any = Field(None, alias='marginBottom', union_mode='left_to_right')

class Facets1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genres: list[str] | Any = Field(None, alias='Genres', union_mode='left_to_right')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tab: UUID | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    facets: Facets1 | Any = Field(default=None, union_mode='left_to_right')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data | Any = Field(default=None, union_mode='left_to_right')

class Attributes2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    is_selected: bool | Any = Field(None, alias='isSelected', union_mode='left_to_right')
    is_small: bool | Any = Field(None, alias='isSmall', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    hide_lock_icon: bool | Any = Field(None, alias='hideLockIcon', union_mode='left_to_right')
    action: Action | Any = Field(default=None, union_mode='left_to_right')

class Tv1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')

class Mobile1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')

class Tablet1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')

class Desktop1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')

class Style2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')
    tv: Tv1 | Any = Field(default=None, union_mode='left_to_right')
    mobile: Mobile1 | Any = Field(default=None, union_mode='left_to_right')
    tablet: Tablet1 | Any = Field(default=None, union_mode='left_to_right')
    desktop: Desktop1 | Any = Field(default=None, union_mode='left_to_right')

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes2 | Any = Field(default=None, union_mode='left_to_right')
    style: Style2 | Any = Field(default=None, union_mode='left_to_right')

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    size: int | Any = Field(default=None, union_mode='left_to_right')

class AfterElement(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes3 | Any = Field(default=None, union_mode='left_to_right')

class Data1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    facets: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data1 | Any = Field(default=None, union_mode='left_to_right')

class ArrowStyle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    background_color: str | Any = Field(None, alias='backgroundColor', union_mode='left_to_right')
    border_radius: str | Any = Field(None, alias='borderRadius', union_mode='left_to_right')
    border_color: str | Any = Field(None, alias='borderColor', union_mode='left_to_right')

class Attributes1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    style: Style1 | Any = Field(default=None, union_mode='left_to_right')
    is_scrollable: bool | Any = Field(None, alias='isScrollable', union_mode='left_to_right')
    buttons: list[Button] | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    accessibility_label: str | Any = Field(None, alias='accessibilityLabel', union_mode='left_to_right')
    after_element: AfterElement | Any = Field(None, alias='afterElement', union_mode='left_to_right')
    action: Action1 | Any = Field(default=None, union_mode='left_to_right')
    is_selected: bool | Any = Field(None, alias='isSelected', union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    is_small: bool | Any = Field(None, alias='isSmall', union_mode='left_to_right')
    is_scrollbar_hidden: bool | Any = Field(None, alias='isScrollbarHidden', union_mode='left_to_right')
    arrow_style: ArrowStyle | Any = Field(None, alias='arrowStyle', union_mode='left_to_right')

class Tv2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')
    padding_start: str | Any = Field(None, alias='paddingStart', union_mode='left_to_right')
    padding_end: str | Any = Field(None, alias='paddingEnd', union_mode='left_to_right')

class Style3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align_self: str | Any = Field(None, alias='alignSelf', union_mode='left_to_right')
    flex_shrink: int | Any = Field(None, alias='flexShrink', union_mode='left_to_right')
    background_color: str | Any = Field(None, alias='backgroundColor', union_mode='left_to_right')
    border_radius: str | Any = Field(None, alias='borderRadius', union_mode='left_to_right')
    display: str | Any = Field(default=None, union_mode='left_to_right')
    tv: Tv2 | Any = Field(default=None, union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Element1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes1 | Any = Field(default=None, union_mode='left_to_right')
    style: Style3 | Any = Field(default=None, union_mode='left_to_right')

class Attributes4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    dynamic_label: str | Any = Field(None, alias='dynamicLabel', union_mode='left_to_right')

class Style4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | Any = Field(default=None, union_mode='left_to_right')
    font_size: int | Any = Field(None, alias='fontSize', union_mode='left_to_right')
    line_height: str | Any = Field(None, alias='lineHeight', union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes4 | Any = Field(default=None, union_mode='left_to_right')
    style: Style4 | Any = Field(default=None, union_mode='left_to_right')

class Tv3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    margin_top: int | Any = Field(None, alias='marginTop', union_mode='left_to_right')

class Style5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    border_bottom_width: int | Any = Field(None, alias='borderBottomWidth', union_mode='left_to_right')
    align_self: str | Any = Field(None, alias='alignSelf', union_mode='left_to_right')
    tv: Tv3 | Any = Field(default=None, union_mode='left_to_right')

class Style6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Tv4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    font_weight: int | Any = Field(None, alias='fontWeight', union_mode='left_to_right')
    color: str | Any = Field(default=None, union_mode='left_to_right')

class Style7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | Any = Field(default=None, union_mode='left_to_right')
    font_weight: int | Any = Field(None, alias='fontWeight', union_mode='left_to_right')
    tv: Tv4 | Any = Field(default=None, union_mode='left_to_right')

class CurrentSearch(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | Any = Field(default=None, union_mode='left_to_right')
    facets_requested: str | Any = Field(None, alias='facetsRequested', union_mode='left_to_right')
    sort: str | Any = Field(default=None, union_mode='left_to_right')
    sort_direction: str | Any = Field(None, alias='sortDirection', union_mode='left_to_right')
    grid_view_config_id: UUID | Any = Field(None, alias='gridViewConfigId', union_mode='left_to_right')

class Data2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    sort: str | Any = Field(default=None, union_mode='left_to_right')
    sort_direction: str | Any = Field(None, alias='sortDirection', union_mode='left_to_right')
    current_search: CurrentSearch | Any = Field(None, alias='currentSearch', union_mode='left_to_right')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data2 | Any = Field(default=None, union_mode='left_to_right')

class Attributes6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    is_small: bool | Any = Field(None, alias='isSmall', union_mode='left_to_right')
    is_selected: bool | Any = Field(None, alias='isSelected', union_mode='left_to_right')
    hide_text_on_mobile: bool | Any = Field(None, alias='hideTextOnMobile', union_mode='left_to_right')
    action: Action2 | Any = Field(default=None, union_mode='left_to_right')

class Button1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    field_variant: str | Any = Field(None, alias='$variant', union_mode='left_to_right')
    style: Style7 | Any = Field(default=None, union_mode='left_to_right')
    attributes: Attributes6 | Any = Field(default=None, union_mode='left_to_right')

class Attributes5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    buttons: list[Button1] | Any = Field(default=None, union_mode='left_to_right')

class ButtonList(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    field_variant: str | Any = Field(None, alias='$variant', union_mode='left_to_right')
    style: Style6 | Any = Field(default=None, union_mode='left_to_right')
    attributes: Attributes5 | Any = Field(default=None, union_mode='left_to_right')

class Option(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    is_visible: bool | Any = Field(None, alias='isVisible', union_mode='left_to_right')
    is_active: bool | Any = Field(None, alias='isActive', union_mode='left_to_right')
    value: str | Any = Field(default=None, union_mode='left_to_right')
    filter_key: str | Any = Field(None, alias='filterKey', union_mode='left_to_right')
    field: str | Any = Field(default=None, union_mode='left_to_right')
    direction: str | Any = Field(default=None, union_mode='left_to_right')

class Data3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data3 | Any = Field(default=None, union_mode='left_to_right')

class Apply(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action: Action3 | Any = Field(default=None, union_mode='left_to_right')

class CurrentSearch1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | Any = Field(default=None, union_mode='left_to_right')
    facets_requested: str | Any = Field(None, alias='facetsRequested', union_mode='left_to_right')
    sort: str | Any = Field(default=None, union_mode='left_to_right')
    sort_direction: str | Any = Field(None, alias='sortDirection', union_mode='left_to_right')
    grid_view_config_id: UUID | Any = Field(None, alias='gridViewConfigId', union_mode='left_to_right')
    last_seen: str | Any = Field(None, alias='lastSeen', union_mode='left_to_right')

class Data4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    current_search: CurrentSearch1 | Any = Field(None, alias='currentSearch', union_mode='left_to_right')

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data4 | Any = Field(default=None, union_mode='left_to_right')

class Next(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action4 | Any = Field(default=None, union_mode='left_to_right')

class Actions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    apply: Apply | Any = Field(default=None, union_mode='left_to_right')
    next: Next | Any = Field(default=None, union_mode='left_to_right')

class CurrentSearch2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | Any = Field(default=None, union_mode='left_to_right')
    facets_requested: str | Any = Field(None, alias='facetsRequested', union_mode='left_to_right')
    sort: str | Any = Field(default=None, union_mode='left_to_right')
    sort_direction: str | Any = Field(None, alias='sortDirection', union_mode='left_to_right')
    grid_view_config_id: UUID | Any = Field(None, alias='gridViewConfigId', union_mode='left_to_right')

class Data5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    current_search: CurrentSearch2 | Any = Field(None, alias='currentSearch', union_mode='left_to_right')

class Action5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data5 | Any = Field(default=None, union_mode='left_to_right')

class Desktop2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | Any = Field(None, alias='sizeType', union_mode='left_to_right')

class Tv5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | Any = Field(None, alias='sizeType', union_mode='left_to_right')

class Tablet2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | Any = Field(None, alias='sizeType', union_mode='left_to_right')

class Mobile2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | Any = Field(None, alias='sizeType', union_mode='left_to_right')

class Breakpoints(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop: Desktop2 | Any = Field(default=None, union_mode='left_to_right')
    tv: Tv5 | Any = Field(default=None, union_mode='left_to_right')
    tablet: Tablet2 | Any = Field(default=None, union_mode='left_to_right')
    mobile: Mobile2 | Any = Field(default=None, union_mode='left_to_right')

class Style8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    auto_width: bool | Any = Field(None, alias='autoWidth', union_mode='left_to_right')
    border_radius: int | Any = Field(None, alias='borderRadius', union_mode='left_to_right')

class Attributes8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    border_radius: int | Any = Field(None, alias='borderRadius', union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')

class HeaderItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes8 | Any = Field(default=None, union_mode='left_to_right')

class Tv6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: int | Any = Field(default=None, union_mode='left_to_right')

class Breakpoints2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tv: Tv6 | Any = Field(default=None, union_mode='left_to_right')

class Style9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    element_padding_top: str | Any = Field(None, alias='elementPaddingTop', union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    number_of_lines: int | Any = Field(None, alias='numberOfLines', union_mode='left_to_right')

class Tablet3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    font_size: int | Any = Field(None, alias='fontSize', union_mode='left_to_right')

class Mobile3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    font_size: int | Any = Field(None, alias='fontSize', union_mode='left_to_right')

class Style10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    tablet: Tablet3 | Any = Field(default=None, union_mode='left_to_right')
    mobile: Mobile3 | Any = Field(default=None, union_mode='left_to_right')

class Element2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes10 | Any = Field(default=None, union_mode='left_to_right')
    style: Style10 | Any = Field(default=None, union_mode='left_to_right')

class Attributes9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    gap: int | Any = Field(default=None, union_mode='left_to_right')
    breakpoints: Breakpoints2 | Any = Field(default=None, union_mode='left_to_right')
    element_padding_top: int | Any = Field(None, alias='elementPaddingTop', union_mode='left_to_right')
    style: Style9 | Any = Field(default=None, union_mode='left_to_right')
    elements: list[Element2] | Any = Field(default=None, union_mode='left_to_right')

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes9 | Any = Field(default=None, union_mode='left_to_right')

class Desktop3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | Any = Field(None, alias='sizeType', union_mode='left_to_right')
    header: list[HeaderItem] | Any = Field(default=None, union_mode='left_to_right')
    content: list[ContentItem] | Any = Field(default=None, union_mode='left_to_right')

class Attributes11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    border_radius: int | Any = Field(None, alias='borderRadius', union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')

class HeaderItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes11 | Any = Field(default=None, union_mode='left_to_right')

class Breakpoints3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tv: Tv6 | Any = Field(default=None, union_mode='left_to_right')

class Style11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    element_padding_top: str | Any = Field(None, alias='elementPaddingTop', union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    number_of_lines: int | Any = Field(None, alias='numberOfLines', union_mode='left_to_right')

class Style12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    tablet: Tablet3 | Any = Field(default=None, union_mode='left_to_right')
    mobile: Mobile3 | Any = Field(default=None, union_mode='left_to_right')

class Element3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes13 | Any = Field(default=None, union_mode='left_to_right')
    style: Style12 | Any = Field(default=None, union_mode='left_to_right')

class Attributes12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    gap: int | Any = Field(default=None, union_mode='left_to_right')
    breakpoints: Breakpoints3 | Any = Field(default=None, union_mode='left_to_right')
    element_padding_top: int | Any = Field(None, alias='elementPaddingTop', union_mode='left_to_right')
    style: Style11 | Any = Field(default=None, union_mode='left_to_right')
    elements: list[Element3] | Any = Field(default=None, union_mode='left_to_right')

class ContentItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes12 | Any = Field(default=None, union_mode='left_to_right')

class Tv7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | Any = Field(None, alias='sizeType', union_mode='left_to_right')
    header: list[HeaderItem1] | Any = Field(default=None, union_mode='left_to_right')
    content: list[ContentItem1] | Any = Field(default=None, union_mode='left_to_right')

class Attributes14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    border_radius: int | Any = Field(None, alias='borderRadius', union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')

class HeaderItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes14 | Any = Field(default=None, union_mode='left_to_right')

class Tv9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gap: int | Any = Field(default=None, union_mode='left_to_right')

class Breakpoints4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tv: Tv9 | Any = Field(default=None, union_mode='left_to_right')

class Style13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    element_padding_top: str | Any = Field(None, alias='elementPaddingTop', union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    number_of_lines: int | Any = Field(None, alias='numberOfLines', union_mode='left_to_right')

class Style14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    tablet: Tablet3 | Any = Field(default=None, union_mode='left_to_right')
    mobile: Mobile3 | Any = Field(default=None, union_mode='left_to_right')

class Element4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes16 | Any = Field(default=None, union_mode='left_to_right')
    style: Style14 | Any = Field(default=None, union_mode='left_to_right')

class Attributes15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    gap: int | Any = Field(default=None, union_mode='left_to_right')
    breakpoints: Breakpoints4 | Any = Field(default=None, union_mode='left_to_right')
    element_padding_top: int | Any = Field(None, alias='elementPaddingTop', union_mode='left_to_right')
    style: Style13 | Any = Field(default=None, union_mode='left_to_right')
    elements: list[Element4] | Any = Field(default=None, union_mode='left_to_right')

class ContentItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes15 | Any = Field(default=None, union_mode='left_to_right')

class Tablet5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | Any = Field(None, alias='sizeType', union_mode='left_to_right')
    header: list[HeaderItem2] | Any = Field(default=None, union_mode='left_to_right')
    content: list[ContentItem2] | Any = Field(default=None, union_mode='left_to_right')

class Attributes17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    border_radius: int | Any = Field(None, alias='borderRadius', union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')

class HeaderItem3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes17 | Any = Field(default=None, union_mode='left_to_right')

class Breakpoints5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tv: Tv9 | Any = Field(default=None, union_mode='left_to_right')

class Style15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    element_padding_top: str | Any = Field(None, alias='elementPaddingTop', union_mode='left_to_right')
    gap: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    number_of_lines: int | Any = Field(None, alias='numberOfLines', union_mode='left_to_right')

class Tablet7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    font_size: int | Any = Field(None, alias='fontSize', union_mode='left_to_right')

class Style16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | Any = Field(default=None, union_mode='left_to_right')
    size: str | Any = Field(default=None, union_mode='left_to_right')
    tablet: Tablet7 | Any = Field(default=None, union_mode='left_to_right')
    mobile: Mobile3 | Any = Field(default=None, union_mode='left_to_right')

class Element5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes19 | Any = Field(default=None, union_mode='left_to_right')
    style: Style16 | Any = Field(default=None, union_mode='left_to_right')

class Attributes18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    align: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    gap: int | Any = Field(default=None, union_mode='left_to_right')
    breakpoints: Breakpoints5 | Any = Field(default=None, union_mode='left_to_right')
    element_padding_top: int | Any = Field(None, alias='elementPaddingTop', union_mode='left_to_right')
    style: Style15 | Any = Field(default=None, union_mode='left_to_right')
    elements: list[Element5] | Any = Field(default=None, union_mode='left_to_right')

class ContentItem3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes18 | Any = Field(default=None, union_mode='left_to_right')

class Mobile6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size_type: str | Any = Field(None, alias='sizeType', union_mode='left_to_right')
    header: list[HeaderItem3] | Any = Field(default=None, union_mode='left_to_right')
    content: list[ContentItem3] | Any = Field(default=None, union_mode='left_to_right')

class Breakpoints1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop: Desktop3 | Any = Field(default=None, union_mode='left_to_right')
    tv: Tv7 | Any = Field(default=None, union_mode='left_to_right')
    tablet: Tablet5 | Any = Field(default=None, union_mode='left_to_right')
    mobile: Mobile6 | Any = Field(default=None, union_mode='left_to_right')

class ContentStyle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    margin_top: int | Any = Field(None, alias='marginTop', union_mode='left_to_right')

class Attributes20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    border_radius: int | Any = Field(None, alias='borderRadius', union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')

class HeaderItem4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes20 | Any = Field(default=None, union_mode='left_to_right')

class ComputedRelease(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    scheduled_at: AwareDatetime | Any = Field(None, alias='scheduledAt', union_mode='left_to_right')
    computed_state: str | Any = Field(None, alias='computedState', union_mode='left_to_right')
    state: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')

class Data6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    computed_releases: list[ComputedRelease] | Any = Field(None, alias='computedReleases', union_mode='left_to_right')

class Action6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data6 | Any = Field(default=None, union_mode='left_to_right')

class Attributes7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid_version: int | Any = Field(None, alias='gridVersion', union_mode='left_to_right')
    style: Style8 | Any = Field(default=None, union_mode='left_to_right')
    breakpoints: Breakpoints1 | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    has_initial_focus: bool | Any = Field(None, alias='hasInitialFocus', union_mode='left_to_right')
    content_style: ContentStyle | Any = Field(None, alias='contentStyle', union_mode='left_to_right')
    header: list[HeaderItem4] | Any = Field(default=None, union_mode='left_to_right')
    action: Action6 | Any = Field(default=None, union_mode='left_to_right')

class Card(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes7 | Any = Field(default=None, union_mode='left_to_right')

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    elements: list[Element1] | Any = Field(default=None, union_mode='left_to_right')
    disable_filter_column_tv: bool | Any = Field(None, alias='disableFilterColumnTv', union_mode='left_to_right')
    align: str | Any = Field(default=None, union_mode='left_to_right')
    title: Title | Any = Field(default=None, union_mode='left_to_right')
    style: Style5 | Any = Field(default=None, union_mode='left_to_right')
    button_list: ButtonList | Any = Field(None, alias='buttonList', union_mode='left_to_right')
    filters: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    options: list[Option] | Any = Field(default=None, union_mode='left_to_right')
    actions: Actions | Any = Field(default=None, union_mode='left_to_right')
    action: Action5 | Any = Field(default=None, union_mode='left_to_right')
    disable_force_focus: bool | Any = Field(None, alias='disableForceFocus', union_mode='left_to_right')
    grid_version: int | Any = Field(None, alias='gridVersion', union_mode='left_to_right')
    breakpoints: Breakpoints | Any = Field(default=None, union_mode='left_to_right')
    cards: list[Card] | Any = Field(default=None, union_mode='left_to_right')

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_zone: str | Any = Field(None, alias='$zone', union_mode='left_to_right')
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    style: Style | Any = Field(default=None, union_mode='left_to_right')
    attributes: Attributes | Any = Field(default=None, union_mode='left_to_right')
    field_variant: str | Any = Field(None, alias='$variant', union_mode='left_to_right')

class ContentGridModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    initial_available_facets: InitialAvailableFacets | Any = Field(None, alias='initialAvailableFacets', union_mode='left_to_right')
    theme: Theme | Any = Field(default=None, union_mode='left_to_right')
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
