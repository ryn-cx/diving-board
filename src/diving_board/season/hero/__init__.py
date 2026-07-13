"""Contains the SeasonHero class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.season.hero.models import SeasonHeroModel


class SeasonHero(BaseExtractor[SeasonHeroModel]):
    """Extract the hero element from Season."""

    _response_model = SeasonHeroModel
