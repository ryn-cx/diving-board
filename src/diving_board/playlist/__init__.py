from typing import Any

from pydantic import BaseModel

from diving_board.playlist import models
from diving_board.playlist.bucket.playlist import (
    models as playlist_bucket_playlist_models,
)
from diving_board.protocol import DivingBoardProtocol


class PlaylistMixin(DivingBoardProtocol):
    def download_playlist(self, playlist_id: int) -> dict[str, Any]:
        # The URL used for the api call can be found on the playlist page for the movie:
        # https://www.hidive.com/playlist/20431
        # Example API URL:
        # https://dce-frontoffice.imggaming.com/api/v1/view?type=playlist&id=20431&timezone=America%2FLos_Angeles

        endpoint = "api/v1/view"
        parms: dict[str, str | int] = {
            "type": "playlist",
            "id": playlist_id,
            "timezone": self.timezone,
        }
        return self._download_api_request(endpoint, parms)

    def parse_playlist(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> models.Playlist:
        if update:
            return self.parse_response(models.Playlist, data, "playlist")

        return models.Playlist.model_validate(data)

    def get_playlist(self, playlist_id: int) -> models.Playlist:
        response = self.download_playlist(playlist_id)
        return self.parse_playlist(response)

    def extract_playlist_bucket_playlist(
        self,
        data: models.Playlist,
        *,
        update: bool = True,
    ) -> playlist_bucket_playlist_models.PlaylistBucketPlaylist:
        return self._extract_playlist_generic(
            data,
            playlist_bucket_playlist_models.PlaylistBucketPlaylist,
            "playlist",
            update=update,
        )

    # TODO: This can be generalized with _extract_season_generic
    def _extract_playlist_generic[T: BaseModel](
        self,
        data: models.Playlist,
        response_model: type[T],
        attribute_type: str,
        *,
        update: bool = True,
    ) -> T:
        for element in data.elements:
            if (
                element.field_type == "bucket"
                and element.attributes.type == attribute_type
            ):
                season_data = element.attributes.model_dump(
                    mode="json",
                    by_alias=True,
                    exclude_unset=True,
                )

                if update:
                    return self.parse_response(
                        response_model,
                        season_data,
                        f"playlist/bucket/{attribute_type}",
                    )

                return response_model.model_validate(season_data)

        msg = "No bucket playlist element found in playlist data"
        raise ValueError(msg)
