# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WrapperCollection"]


class WrapperCollection(BaseModel):
    data: Optional[List[object]] = None
    """The wrapper for a collection is an array of objects."""

    links: Optional[object] = None
    """A set of hypermedia links which serve as controls for the client."""
