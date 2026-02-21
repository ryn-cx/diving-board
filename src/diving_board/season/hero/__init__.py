"""Season hero extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.hero.model import SeasonHeroModel


class SeasonHero(BaseExtractor[SeasonHeroModel]):
    """Extracts data from Season where field_type=hero."""

    _response_model = SeasonHeroModel
