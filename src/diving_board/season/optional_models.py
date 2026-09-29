from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Attributes1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes1 | Any = Field(default=None, union_mode='left_to_right')

class Attributes2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes2 | Any = Field(default=None, union_mode='left_to_right')

class Token(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | Any = Field(default=None, union_mode='left_to_right')
    value: str | Any = Field(default=None, union_mode='left_to_right')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    video_id: int | Any = Field(None, alias='videoId', union_mode='left_to_right')
    online_playback: str | Any = Field(None, alias='onlinePlayback', union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')
    series_id: int | Any = Field(None, alias='seriesId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data | Any = Field(default=None, union_mode='left_to_right')

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_initial_focus: bool | Any = Field(None, alias='hasInitialFocus', union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    tokens: list[Token] | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action1 | Any = Field(default=None, union_mode='left_to_right')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes3 | Any = Field(default=None, union_mode='left_to_right')

class Attributes5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Tag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes5 | Any = Field(default=None, union_mode='left_to_right')

class Data1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    universal_link: str | Any = Field(None, alias='universalLink', union_mode='left_to_right')
    tracking_parameters: list[Any] | Any = Field(None, alias='trackingParameters', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data1 | Any = Field(default=None, union_mode='left_to_right')

class Attributes6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action2 | Any = Field(default=None, union_mode='left_to_right')

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes6 | Any = Field(default=None, union_mode='left_to_right')

class Attributes4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: list[Tag] | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    buttons: list[Button] | Any = Field(default=None, union_mode='left_to_right')

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes4 | Any = Field(default=None, union_mode='left_to_right')

class Data2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tab: str | Any = Field(default=None, union_mode='left_to_right')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data2 | Any = Field(default=None, union_mode='left_to_right')

class Attributes7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action3 | Any = Field(default=None, union_mode='left_to_right')

class ContentDownload(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    permission: str | Any = Field(default=None, union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes7 | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    content_download: ContentDownload | Any = Field(None, alias='contentDownload', union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    long_description: str | Any = Field(None, alias='longDescription', union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    thumbnail_url: str | Any = Field(None, alias='thumbnailUrl', union_mode='left_to_right')
    max_height: int | Any = Field(None, alias='maxHeight', union_mode='left_to_right')
    online_playback: str | Any = Field(None, alias='onlinePlayback', union_mode='left_to_right')
    computed_releases: list[Any] | Any = Field(None, alias='computedReleases', union_mode='left_to_right')
    watch_status: str | Any = Field(None, alias='watchStatus', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    cover_url: str | Any = Field(None, alias='coverUrl', union_mode='left_to_right')
    season_count: str | Any = Field(None, alias='seasonCount', union_mode='left_to_right')
    small_cover_url: str | Any = Field(None, alias='smallCoverUrl', union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    favourite: bool | Any = Field(default=None, union_mode='left_to_right')
    favourite_channel: str | Any = Field(None, alias='favouriteChannel', union_mode='left_to_right')
    has_permission: bool | Any = Field(None, alias='hasPermission', union_mode='left_to_right')
    is_related: bool | Any = Field(None, alias='isRelated', union_mode='left_to_right')
    has_permission_granted_on_sign_in: bool | Any = Field(None, alias='hasPermissionGrantedOnSignIn', union_mode='left_to_right')

class Series(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    series_id: int | Any = Field(None, alias='seriesId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    long_description: str | Any = Field(None, alias='longDescription', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    episode_count: int | Any = Field(None, alias='episodeCount', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    series: Series | Any = Field(default=None, union_mode='left_to_right')

class Paging(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    more_data_available: bool | Any = Field(None, alias='moreDataAvailable', union_mode='left_to_right')

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item1] | Any = Field(default=None, union_mode='left_to_right')
    paging: Paging | Any = Field(default=None, union_mode='left_to_right')

class Paging1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    more_data_available: bool | Any = Field(None, alias='moreDataAvailable', union_mode='left_to_right')
    last_seen: int | str | Any = Field(None, alias='lastSeen', union_mode='left_to_right')

class GroupName(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header | Any = Field(default=None, union_mode='left_to_right')
    image: Image | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action] | Any = Field(default=None, union_mode='left_to_right')
    content: list[ContentItem] | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    active_tab: str | Any = Field(None, alias='activeTab', union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    tab: str | Any = Field(default=None, union_mode='left_to_right')
    series: Series | Any = Field(default=None, union_mode='left_to_right')
    season_id: int | Any = Field(None, alias='seasonId', union_mode='left_to_right')
    seasons: Seasons | Any = Field(default=None, union_mode='left_to_right')
    row_position: int | Any = Field(None, alias='rowPosition', union_mode='left_to_right')
    bucket_title: str | Any = Field(None, alias='bucketTitle', union_mode='left_to_right')
    series_id: int | Any = Field(None, alias='seriesId', union_mode='left_to_right')
    paging: Paging1 | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    group_name: GroupName | Any = Field(None, alias='groupName', union_mode='left_to_right')
    display_mode: str | Any = Field(None, alias='displayMode', union_mode='left_to_right')
    tab_spacing: int | Any = Field(None, alias='tabSpacing', union_mode='left_to_right')
    active_underline_color: str | Any = Field(None, alias='activeUnderlineColor', union_mode='left_to_right')
    hover_underline_color: str | Any = Field(None, alias='hoverUnderlineColor', union_mode='left_to_right')

class Desktop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')

class Tv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')

class Mobile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')

class Tablet(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop: Desktop | Any = Field(default=None, union_mode='left_to_right')
    tv: Tv | Any = Field(default=None, union_mode='left_to_right')
    mobile: Mobile | Any = Field(default=None, union_mode='left_to_right')
    tablet: Tablet | Any = Field(default=None, union_mode='left_to_right')

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    field_zone: str | Any = Field(None, alias='$zone', union_mode='left_to_right')
    attributes: Attributes | Any = Field(default=None, union_mode='left_to_right')
    style: Style | Any = Field(default=None, union_mode='left_to_right')

class CurrentSeason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    season_id: int | Any = Field(None, alias='seasonId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class CurrentVod(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    season_id: int | Any = Field(None, alias='seasonId', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    series: Series | Any = Field(default=None, union_mode='left_to_right')
    current_season: CurrentSeason | Any = Field(None, alias='currentSeason', union_mode='left_to_right')
    current_vod: CurrentVod | Any = Field(None, alias='currentVod', union_mode='left_to_right')

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

class SeasonModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    layout: str | Any = Field(default=None, union_mode='left_to_right')
    elements: list[Element] | Any = Field(default=None, union_mode='left_to_right')
    metadata: Metadata | Any = Field(default=None, union_mode='left_to_right')
    theme: Theme | Any = Field(default=None, union_mode='left_to_right')
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
