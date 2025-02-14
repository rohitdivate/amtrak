# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .booking import Booking
from .links_self import LinksSelf
from .links_pagination import LinksPagination
from .wrapper_collection import WrapperCollection

__all__ = ["BookingListResponse", "BookingListResponseLinks"]


class BookingListResponseLinks(LinksSelf, LinksPagination):
    pass


class BookingListResponse(WrapperCollection):
    data: Optional[List[Booking]] = None  # type: ignore

    links: Optional[BookingListResponseLinks] = None  # type: ignore
