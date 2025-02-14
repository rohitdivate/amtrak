# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .links_self import LinksSelf
from .links_pagination import LinksPagination
from .wrapper_collection import WrapperCollection

__all__ = ["ListTripListTripsResponse", "ListTripListTripsResponseData", "ListTripListTripsResponseLinks"]


class ListTripListTripsResponseData(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the trip"""

    arrival_time: Optional[datetime] = None
    """The date and time when the trip arrives"""

    bicycles_allowed: Optional[bool] = None
    """Indicates whether bicycles are allowed on the trip"""

    departure_time: Optional[datetime] = None
    """The date and time when the trip departs"""

    destination: Optional[str] = None
    """The destination station of the trip"""

    dogs_allowed: Optional[bool] = None
    """Indicates whether dogs are allowed on the trip"""

    operator: Optional[str] = None
    """The name of the operator of the trip"""

    origin: Optional[str] = None
    """The starting station of the trip"""

    price: Optional[float] = None
    """The cost of the trip"""

    self: Optional[str] = None


class ListTripListTripsResponseLinks(LinksSelf, LinksPagination):
    pass


class ListTripListTripsResponse(WrapperCollection):
    data: Optional[List[ListTripListTripsResponseData]] = None  # type: ignore

    links: Optional[ListTripListTripsResponseLinks] = None  # type: ignore
