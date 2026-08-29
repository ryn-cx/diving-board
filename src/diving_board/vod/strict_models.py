from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field

class Attributes1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class Header(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes1

class Attributes2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes2

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    access_level: str = Field(..., alias='accessLevel')
    licence_ids: list[int] = Field(..., alias='licenceIds')
    id: int
    title: str
    type: str

class Action1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data

class Attributes3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    has_initial_focus: bool = Field(..., alias='hasInitialFocus')
    text: str
    label: str
    icon: str
    action: Action1

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes3

class Attributes5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str | None = None

class Tag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes5

class Data1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    title: str
    type: str

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data1

class Attributes6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    text: str
    label: str
    icon: str
    action: Action2

class Button(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes6

class Attributes4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: list[Tag] | None = None
    text: str | None = None
    id: int | None = None
    progress: None = None
    duration: int | None = None
    watch_status: str | None = Field(None, alias='watchStatus')
    buttons: list[Button] | None = None

class Style(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str

class ContentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    attributes: Attributes4
    style: Style | None = None

class Data2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tab: str

class Action3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data2

class Attributes7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    label: str
    action: Action3

class ContentDownload(BaseModel):
    model_config = ConfigDict(defer_build=True)
    permission: str

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    model_config = ConfigDict(defer_build=True)
    text: str
    label: str

class Paging(BaseModel):
    model_config = ConfigDict(defer_build=True)
    more_data_available: bool = Field(..., alias='moreDataAvailable')
    last_seen: str = Field(..., alias='lastSeen')

class Attributes(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    model_config = ConfigDict(defer_build=True)
    display: str

class Tv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str

class Mobile(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str

class Tablet(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display: str

class Style1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    desktop: Desktop | None = None
    tv: Tv | None = None
    mobile: Mobile | None = None
    tablet: Tablet | None = None

class Element(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='$type')
    field_zone: str = Field(..., alias='$zone')
    attributes: Attributes
    style: Style1 | None = None

class VodModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
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
