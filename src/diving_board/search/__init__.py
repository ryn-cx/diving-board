# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from diving_board.base_api_endpoint import BaseEndpoint
from diving_board.search.models import SearchModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Search(BaseEndpoint):
    """Contains the search.

    Search is answered by a host of its own, but what comes back is the same
    kind of view as the rest of the API answers with.

    Source: https://www.hidive.com/search

    Example request:
        - GET /search?
            - query={query}&
            - timezone=America%2FLos_Angeles
            - HTTP/2
        - Host: search.dce-prod.dicelaboratory.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/plain, */*
        - Referer: https://www.hidive.com/
        - Origin: https://www.hidive.com
        - x-api-key: __REDACTED__
        - app: dice
        - Realm: dce.hidive
        - Authorization: Bearer __REDACTED__
    """

    # TODO: Validate
    def __call__(self, query: str, *, timezone: str | None = None) -> SearchModel:
        """Download and parse the search file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(query, timezone=timezone), log_id)

    # TODO: Validate
    def download(self, query: str, *, timezone: str | None = None) -> str:
        """Download the search file.

        A query nothing matches is answered with the same view carrying no
        cards, so it comes back as a file like any other.
        """
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            "https://search.dce-prod.dicelaboratory.com/search",
            params={
                "query": query,
                "timezone": timezone or self._client.timezone,
            },
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SearchModel:
        """Load a search file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
