# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Knowledge"]


class Knowledge(BaseModel):
    id: str

    created_at: str

    name: str

    object: Literal["knowledge"]

    status: Literal["pending", "partial", "ready", "failed"]
