# TODO: Validate
"""Contains the VodHero class."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.hero.models import VodHeroModel


class VodHero(BaseExtractor[VodHeroModel]):
    """Extract the hero element from Vod."""

    _response_model = VodHeroModel
