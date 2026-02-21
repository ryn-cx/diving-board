"""Vod hero extractor."""

from __future__ import annotations

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.hero.model import VodHeroModel


class VodHero(BaseExtractor[VodHeroModel]):
    """Extracts data from Vod where field_type=hero."""

    _response_model = VodHeroModel
