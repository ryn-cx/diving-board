"""Vod hero extractor."""

from __future__ import annotations

from functools import cached_property
from typing import override

from diving_board.base_api_endpoint import BaseExtractor
from diving_board.vod.hero.model import VodHeroModel


class VodHero(BaseExtractor[VodHeroModel]):
    """Provides methods to manage the hero element from vod data."""

    @cached_property
    @override
    def _response_model(self) -> type[VodHeroModel]:
        return VodHeroModel
