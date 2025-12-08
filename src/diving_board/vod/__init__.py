from datetime import datetime
from typing import Any

from pydantic import BaseModel

from diving_board.protocol import DivingBoardProtocol
from diving_board.vod import models
from diving_board.vod.bucket import models as bucket_models
from diving_board.vod.hero import models as hero_models
from diving_board.vod.tabs import models as tabs_models
from diving_board.vod.text_block import models as text_block_models


class VodMixin(DivingBoardProtocol):
    def download_vod(self, vod_id: int) -> dict[str, Any]:
        # The URL used for the api call can be found on the episode interstitial page:
        # https://www.hidive.com/interstitial/532182
        # Example API URL:
        # https://dce-frontoffice.imggaming.com/api/v1/view?type=vod&id=532182&timezone=America%2FLos_Angeles
        endpoint = "api/v1/view"
        params: dict[str, str | int] = {
            "type": "vod",
            "id": vod_id,
            "timezone": self.timezone,
        }
        return self._download_api_request(endpoint, params)

    def parse_vod(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> models.Vod:
        if update:
            return self.parse_response(models.Vod, data, "vod")

        return models.Vod.model_validate(data)

    def get_vod(self, vod_id: int) -> models.Vod:
        data = self.download_vod(vod_id)
        return self.parse_vod(data)

    def extract_vod_original_premiere(
        self,
        data: models.Vod,
    ) -> datetime:
        """Extract the Original Premiere date from a VOD.

        Args:
            data: VOD data

        Returns:
            Original premiere date string or None if not found
        """
        for element in data.elements:
            if element.field_type == "hero":
                for content_item in element.attributes.content or []:
                    if content_item.field_type == "tagList":
                        # Search through tags for "Original Premiere: ..."
                        for tag in content_item.attributes.tags or []:
                            if (
                                tag.field_type == "textblock"
                                and tag.attributes.text
                                and tag.attributes.text.startswith("Original Premiere:")
                            ):
                                # Extract the date portion after "Original Premiere: "
                                date_string = tag.attributes.text
                                date = date_string.replace("Original Premiere: ", "")
                                return datetime.strptime(date, "%B %d, %Y").astimezone()

        msg = "Original Premiere date not found in VOD data"
        raise ValueError(msg)

    def extract_vod_hero(
        self,
        data: models.Vod,
        *,
        update: bool = True,
    ) -> hero_models.VodHero:
        return self._extract_vod_entry(
            hero_models.VodHero,
            "hero",
            data,
            update=update,
        )

    def extract_vod_bucket(
        self,
        data: models.Vod,
        *,
        update: bool = True,
    ) -> bucket_models.VodBucket:
        return self._extract_vod_entry(
            bucket_models.VodBucket,
            "bucket",
            data,
            update=update,
        )

    def extract_vod_tabs(
        self,
        data: models.Vod,
        *,
        update: bool = True,
    ) -> tabs_models.VodTabs:
        return self._extract_vod_entry(
            tabs_models.VodTabs,
            "tabs",
            data,
            update=update,
        )

    def extract_vod_text_block(
        self,
        data: models.Vod,
        *,
        update: bool = True,
    ) -> text_block_models.VodTextBlock:
        return self._extract_vod_entry(
            text_block_models.VodTextBlock,
            "textBlock",
            data,
            update=update,
            field_name="text_block",
        )

    # TODO: Consider removing requirement for both field_type and field_name and require
    # only one or the other.
    def _extract_vod_entry[T: BaseModel](
        self,
        response_model: type[T],
        field_type: str,
        data: models.Vod,
        *,
        field_name: str | None = None,
        update: bool = True,
    ) -> T:
        if field_name is None:
            field_name = field_type

        for element in data.elements:
            if element.field_type == field_type:
                dumped_element = element.model_dump(mode="json")

                if update:
                    return self.parse_response(
                        response_model,
                        dumped_element,
                        f"vod/{field_name}",
                    )

                return response_model.model_validate(dumped_element)

        msg = f"No {field_type} element found in VOD data"
        raise ValueError(msg)
