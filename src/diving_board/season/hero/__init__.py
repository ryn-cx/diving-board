"""Season hero extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.hero.model import SeasonHeroModel


class SeasonHero(BaseExtractor[SeasonHeroModel]):
    """Provides methods to manage the hero element from season data."""

    @cached_property
    @override
    def _response_model(self) -> type[SeasonHeroModel]:
        return SeasonHeroModel
