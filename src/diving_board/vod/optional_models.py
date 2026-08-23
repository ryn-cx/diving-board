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

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore')
    access_level: str | None = Field(None, alias='accessLevel')
    licence_ids: list[int] | None = Field(None, alias='licenceIds')
    id: int | None = None
    title: str | None = None
    type: str | None = None

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    data: Data | None = None

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    has_initial_focus: bool | None = Field(None, alias='hasInitialFocus')
    text: str | None = None
    label: str | None = None
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
    title: str | None = None
    type: str | None = None

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
    id: int | None = None
    progress: Any | None = None
    duration: int | None = None
    watch_status: str | None = Field(None, alias='watchStatus')
    buttons: list[Button] | None = None

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display: str | None = None

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='$type')
    attributes: Attributes4 | None = None
    style: Style | None = None

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
    id: int | None = None
    type: str | None = None
    title: str | None = None
    description: str | None = None
    long_description: str | None = Field(None, alias='longDescription')
    content_download: ContentDownload | None = Field(None, alias='contentDownload')
    cover_url: str | None = Field(None, alias='coverUrl')
    small_cover_url: str | None = Field(None, alias='smallCoverUrl')
    season_count: str | None = Field(None, alias='seasonCount')
    poster_url: str | None = Field(None, alias='posterUrl')
    access_level: str | None = Field(None, alias='accessLevel')
    favourite: bool | None = None
    watch_status: str | None = Field(None, alias='watchStatus')
    favourite_channel: str | None = Field(None, alias='favouriteChannel')
    has_permission: bool | None = Field(None, alias='hasPermission')
    is_related: bool | None = Field(None, alias='isRelated')
    has_permission_granted_on_sign_in: bool | None = Field(None, alias='hasPermissionGrantedOnSignIn')

class GroupName(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    label: str | None = None

class Paging(BaseModel):
    model_config = ConfigDict(extra='ignore')
    more_data_available: bool | None = Field(None, alias='moreDataAvailable')
    last_seen: str | None = Field(None, alias='lastSeen')

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore')
    header: Header | None = None
    image: Image | None = None
    actions: list[Action] | None = None
    content: list[ContentItem] | None = None
    type: str | None = None
    id: int | None = None
    active_tab: str | None = Field(None, alias='activeTab')
    items: list[Item] | None = None
    text: str | None = None
    label: str | None = None
    tab: str | None = None
    bucket_title: str | None = Field(None, alias='bucketTitle')
    group_name: GroupName | None = Field(None, alias='groupName')
    paging: Paging | None = None

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

class Style1(BaseModel):
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
    style: Style1 | None = None

class VodModel(BaseModel):
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
