# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["KnowledgeListParams"]


class KnowledgeListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]

    limit: int

    next: str

    sort: Literal["created_at"]
