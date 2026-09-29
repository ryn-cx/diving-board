# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import AdjacentSeriesModel as OptionalModel
from .strict_models import AdjacentSeriesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        AdjacentSeriesModel,
        FollowingItem,
        FollowingSeason,
        PrecedingItem,
        PrecedingSeason,
        WatchOrder,
    )
else:
    from .optional_models import (
        AdjacentSeriesModel,
        FollowingItem,
        FollowingSeason,
        PrecedingItem,
        PrecedingSeason,
        WatchOrder,
    )

__all__ = [
    "AdjacentSeriesModel",
    "FollowingItem",
    "FollowingSeason",
    "PrecedingItem",
    "PrecedingSeason",
    "WatchOrder",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> AdjacentSeriesModel:
    """Read a downloaded file into AdjacentSeriesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
