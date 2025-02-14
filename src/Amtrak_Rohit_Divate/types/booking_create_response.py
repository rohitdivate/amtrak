# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .booking import Booking
from .links_self import LinksSelf

__all__ = ["BookingCreateResponse"]


class BookingCreateResponse(Booking):
    links: Optional[LinksSelf] = None
