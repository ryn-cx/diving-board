from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Attributes1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes1 | None = None

class Attributes2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    source: str | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes2 | None = None

class Token(BaseModel):
    model_config = ConfigDict(extra='ignore')
    key: str | None = None
    value: str | None = None

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: int | None = None
    video_id: int | None = Field(None, alias='videoId')
    online_playback: str | None = Field(None, alias='onlinePlayback')
    access_level: str | None = Field(None, alias='accessLevel')
    series_id: int | None = Field(None, alias='seriesId')
    title: str | None = None
    type: str | None = None

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    data: Data | None = None

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    has_initial_focus: bool | None = Field(None, alias='hasInitialFocus')
    text: str | None = None
    label: str | None = None
    tokens: list[Token] | None = None
    type: str | None = None
    icon: str | None = None
    action: Action1 | None = None

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes3 | None = None

class Attributes5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None

class Tag(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes5 | None = None

class Data1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: int | None = None
    type: str | None = None
    universal_link: str | None = Field(None, alias='universalLink')
    tracking_parameters: list[Any] | None = Field(None, alias='trackingParameters')
    title: str | None = None

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    data: Data1 | None = None

class Attributes6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    text: str | None = None
    label: str | None = None
    icon: str | None = None
    action: Action2 | None = None

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes6 | None = None

class Attributes4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tags: list[Tag] | None = None
    text: str | None = None
    buttons: list[Button] | None = None

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes4 | None = None

class Data2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    tab: str | None = None

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    data: Data2 | None = None

class Attributes7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    label: str | None = None
    action: Action3 | None = None

class ContentDownload(BaseModel):
    model_config = ConfigDict(extra='ignore')
    permission: str | None = None

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes7 | None = None
    title: str | None = None
    access_level: str | None = Field(None, alias='accessLevel')
    type: str | None = None
    content_download: ContentDownload | None = Field(None, alias='contentDownload')
    description: str | None = None
    long_description: str | None = Field(None, alias='longDescription')
    duration: int | None = None
    thumbnail_url: str | None = Field(None, alias='thumbnailUrl')
    max_height: int | None = Field(None, alias='maxHeight')
    online_playback: str | None = Field(None, alias='onlinePlayback')
    computed_releases: list[Any] | None = Field(None, alias='computedReleases')
    watch_status: str | None = Field(None, alias='watchStatus')
    id: int | None = None
    cover_url: str | None = Field(None, alias='coverUrl')
    season_count: str | None = Field(None, alias='seasonCount')
    small_cover_url: str | None = Field(None, alias='smallCoverUrl')
    poster_url: str | None = Field(None, alias='posterUrl')
    favourite: bool | None = None
    favourite_channel: str | None = Field(None, alias='favouriteChannel')
    has_permission: bool | None = Field(None, alias='hasPermission')
    is_related: bool | None = Field(None, alias='isRelated')
    has_permission_granted_on_sign_in: bool | None = Field(None, alias='hasPermissionGrantedOnSignIn')

class Series(BaseModel):
    model_config = ConfigDict(extra='ignore')
    series_id: int | None = Field(None, alias='seriesId')
    title: str | None = None

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: str | None = None
    description: str | None = None
    long_description: str | None = Field(None, alias='longDescription')
    season_number: int | None = Field(None, alias='seasonNumber')
    episode_count: int | None = Field(None, alias='episodeCount')
    id: int | None = None
    series: Series | None = None

class Paging(BaseModel):
    model_config = ConfigDict(extra='ignore')
    more_data_available: bool | None = Field(None, alias='moreDataAvailable')
    last_seen: int | None = Field(None, alias='lastSeen')

class Seasons(BaseModel):
    model_config = ConfigDict(extra='ignore')
    items: list[Item1] | None = None
    paging: Paging | None = None

class Paging1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    more_data_available: bool | None = Field(None, alias='moreDataAvailable')
    last_seen: int | str | None = Field(None, alias='lastSeen')

class GroupName(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    label: str | None = None

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore')
    header: Header | None = None
    image: Image | None = None
    actions: list[Action] | None = None
    content: list[ContentItem] | None = None
    id: int | None = None
    type: str | None = None
    active_tab: str | None = Field(None, alias='activeTab')
    items: list[Item] | None = None
    tab: str | None = None
    series: Series | None = None
    season_id: int | None = Field(None, alias='seasonId')
    seasons: Seasons | None = None
    row_position: int | None = Field(None, alias='rowPosition')
    bucket_title: str | None = Field(None, alias='bucketTitle')
    series_id: int | None = Field(None, alias='seriesId')
    paging: Paging1 | None = None
    text: str | None = None
    label: str | None = None
    group_name: GroupName | None = Field(None, alias='groupName')

class Desktop(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display: str | None = None

class Tv(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display: str | None = None

class Mobile(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display: str | None = None

class Tablet(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display: str | None = None

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore')
    desktop: Desktop | None = None
    tv: Tv | None = None
    mobile: Mobile | None = None
    tablet: Tablet | None = None

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    field_zone: str | None = Field(None, alias='$zone')
    attributes: Attributes | None = None
    style: Style | None = None

class CurrentSeason(BaseModel):
    model_config = ConfigDict(extra='ignore')
    season_id: int | None = Field(None, alias='seasonId')
    title: str | None = None

class CurrentVod(BaseModel):
    model_config = ConfigDict(extra='ignore')
    season_id: int | None = Field(None, alias='seasonId')
    title: str | None = None

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    series: Series | None = None
    current_season: CurrentSeason | None = Field(None, alias='currentSeason')
    current_vod: CurrentVod | None = Field(None, alias='currentVod')

class SeriesModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    source: str | None = None
    layout: str | None = None
    elements: list[Element] | None = None
    metadata: Metadata | None = None
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
