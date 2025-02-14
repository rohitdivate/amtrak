# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .links_self import LinksSelf
from .links_pagination import LinksPagination
from .wrapper_collection import WrapperCollection

__all__ = [
    "ListStationListStationsResponse",
    "ListStationListStationsResponseData",
    "ListStationListStationsResponseLinks",
]


class ListStationListStationsResponseData(BaseModel):
    id: str
    """Unique identifier for the station."""

    address: str
    """The address of the station."""

    country_code: str
    """The country code of the station."""

    name: str
    """The name of the station"""

    timezone: Optional[str] = None
    """
    The timezone of the station in the
    [IANA Time Zone Database format](https://www.iana.org/time-zones).
    """


class ListStationListStationsResponseLinks(LinksSelf, LinksPagination):
    pass


class ListStationListStationsResponse(WrapperCollection):
    data: Optional[List[ListStationListStationsResponseData]] = None  # type: ignore

    links: Optional[ListStationListStationsResponseLinks] = None  # type: ignore
