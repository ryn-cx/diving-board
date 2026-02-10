# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class VodTabs(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    gapi_sentinel: None
