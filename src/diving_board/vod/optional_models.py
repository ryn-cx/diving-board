from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
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

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')
    licence_ids: list[int] | Any = Field(None, alias='licenceIds', union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data | Any = Field(default=None, union_mode='left_to_right')

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    has_initial_focus: bool | Any = Field(None, alias='hasInitialFocus', union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action1 | Any = Field(default=None, union_mode='left_to_right')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes3 | Any = Field(default=None, union_mode='left_to_right')

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    style: Style | Any = Field(default=None, union_mode='left_to_right')
    attributes: Attributes6 | Any = Field(default=None, union_mode='left_to_right')

class Attributes5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Text | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Style1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | Any = Field(default=None, union_mode='left_to_right')

class Tag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes5 | Any = Field(default=None, union_mode='left_to_right')
    style: Style1 | Any = Field(default=None, union_mode='left_to_right')

class Data1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data1 | Any = Field(default=None, union_mode='left_to_right')

class Attributes7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action2 | Any = Field(default=None, union_mode='left_to_right')

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes7 | Any = Field(default=None, union_mode='left_to_right')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data1 | Any = Field(default=None, union_mode='left_to_right')

class Attributes8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action3 | Any = Field(default=None, union_mode='left_to_right')

class Element1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes8 | Any = Field(default=None, union_mode='left_to_right')

class Attributes4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: list[Tag] | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    progress: Any | None = None
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    watch_status: str | Any = Field(None, alias='watchStatus', union_mode='left_to_right')
    buttons: list[Button] | Any = Field(default=None, union_mode='left_to_right')
    target_date: AwareDatetime | Any = Field(None, alias='targetDate', union_mode='left_to_right')
    elements: list[Element1] | Any = Field(default=None, union_mode='left_to_right')

class Style2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display: str | Any = Field(default=None, union_mode='left_to_right')
    size: float | Any = Field(default=None, union_mode='left_to_right')

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes4 | Any = Field(default=None, union_mode='left_to_right')
    style: Style2 | Any = Field(default=None, union_mode='left_to_right')

class Data3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tab: str | Any = Field(default=None, union_mode='left_to_right')

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data3 | Any = Field(default=None, union_mode='left_to_right')

class Attributes9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    action: Action4 | Any = Field(default=None, union_mode='left_to_right')

class ContentDownload(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    permission: str | Any = Field(default=None, union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | Any = Field(None, alias='$type', union_mode='left_to_right')
    attributes: Attributes9 | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    long_description: str | Any = Field(None, alias='longDescription', union_mode='left_to_right')
    content_download: ContentDownload | Any = Field(None, alias='contentDownload', union_mode='left_to_right')
    cover_url: str | Any = Field(None, alias='coverUrl', union_mode='left_to_right')
    small_cover_url: str | Any = Field(None, alias='smallCoverUrl', union_mode='left_to_right')
    season_count: str | Any = Field(None, alias='seasonCount', union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    access_level: str | Any = Field(None, alias='accessLevel', union_mode='left_to_right')
    favourite: bool | Any = Field(default=None, union_mode='left_to_right')
    watch_status: str | Any = Field(None, alias='watchStatus', union_mode='left_to_right')
    favourite_channel: str | Any = Field(None, alias='favouriteChannel', union_mode='left_to_right')
    has_permission: bool | Any = Field(None, alias='hasPermission', union_mode='left_to_right')
    is_related: bool | Any = Field(None, alias='isRelated', union_mode='left_to_right')
    has_permission_granted_on_sign_in: bool | Any = Field(None, alias='hasPermissionGrantedOnSignIn', union_mode='left_to_right')

class GroupName(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')

class Paging(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    more_data_available: bool | Any = Field(None, alias='moreDataAvailable', union_mode='left_to_right')
    last_seen: str | Any = Field(None, alias='lastSeen', union_mode='left_to_right')

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header | Any = Field(default=None, union_mode='left_to_right')
    image: Image | Any = Field(default=None, union_mode='left_to_right')
    actions: list[Action] | Any = Field(default=None, union_mode='left_to_right')
    content: list[ContentItem] | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    active_tab: str | Any = Field(None, alias='activeTab', union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    tab: str | Any = Field(default=None, union_mode='left_to_right')
    bucket_title: str | Any = Field(None, alias='bucketTitle', union_mode='left_to_right')
    group_name: GroupName | Any = Field(None, alias='groupName', union_mode='left_to_right')
    paging: Paging | Any = Field(default=None, union_mode='left_to_right')

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

class Style3(BaseModel):
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
    style: Style3 | Any = Field(default=None, union_mode='left_to_right')

class VodModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
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
