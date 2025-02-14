# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LinksPagination"]


class LinksPagination(BaseModel):
    next: Optional[str] = None

    prev: Optional[str] = None
