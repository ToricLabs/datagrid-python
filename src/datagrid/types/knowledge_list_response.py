# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .knowledge import Knowledge

__all__ = ["KnowledgeListResponse"]


class KnowledgeListResponse(BaseModel):
    data: List[Knowledge]

    next: str

    object: Literal["list"]
