# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import list_trip_list_trips_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.list_trip_list_trips_response import ListTripListTripsResponse

__all__ = ["ListTripsResource", "AsyncListTripsResource"]


class ListTripsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListTripsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rohitdivate/amtrak#accessing-raw-response-data-eg-headers
        """
        return ListTripsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListTripsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rohitdivate/amtrak#with_streaming_response
        """
        return ListTripsResourceWithStreamingResponse(self)

    def list_trips(
        self,
        *,
        date: Union[str, datetime],
        destination: str,
        origin: str,
        bicycles: bool | NotGiven = NOT_GIVEN,
        dogs: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListTripListTripsResponse:
        """
        Returns a list of available train trips between the specified origin and
        destination stations on the given date, and allows for filtering by bicycle and
        dog allowances.

        Args:
          date: The date and time of the trip in ISO 8601 format in origin station's timezone.

          destination: The ID of the destination station

          origin: The ID of the origin station

          bicycles: Only return trips where bicycles are known to be allowed

          dogs: Only return trips where dogs are known to be allowed

          limit: The number of items to return per page

          page: The page number to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/trips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "destination": destination,
                        "origin": origin,
                        "bicycles": bicycles,
                        "dogs": dogs,
                        "limit": limit,
                        "page": page,
                    },
                    list_trip_list_trips_params.ListTripListTripsParams,
                ),
            ),
            cast_to=ListTripListTripsResponse,
        )


class AsyncListTripsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListTripsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rohitdivate/amtrak#accessing-raw-response-data-eg-headers
        """
        return AsyncListTripsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListTripsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rohitdivate/amtrak#with_streaming_response
        """
        return AsyncListTripsResourceWithStreamingResponse(self)

    async def list_trips(
        self,
        *,
        date: Union[str, datetime],
        destination: str,
        origin: str,
        bicycles: bool | NotGiven = NOT_GIVEN,
        dogs: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListTripListTripsResponse:
        """
        Returns a list of available train trips between the specified origin and
        destination stations on the given date, and allows for filtering by bicycle and
        dog allowances.

        Args:
          date: The date and time of the trip in ISO 8601 format in origin station's timezone.

          destination: The ID of the destination station

          origin: The ID of the origin station

          bicycles: Only return trips where bicycles are known to be allowed

          dogs: Only return trips where dogs are known to be allowed

          limit: The number of items to return per page

          page: The page number to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/trips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "destination": destination,
                        "origin": origin,
                        "bicycles": bicycles,
                        "dogs": dogs,
                        "limit": limit,
                        "page": page,
                    },
                    list_trip_list_trips_params.ListTripListTripsParams,
                ),
            ),
            cast_to=ListTripListTripsResponse,
        )


class ListTripsResourceWithRawResponse:
    def __init__(self, list_trips: ListTripsResource) -> None:
        self._list_trips = list_trips

        self.list_trips = to_raw_response_wrapper(
            list_trips.list_trips,
        )


class AsyncListTripsResourceWithRawResponse:
    def __init__(self, list_trips: AsyncListTripsResource) -> None:
        self._list_trips = list_trips

        self.list_trips = async_to_raw_response_wrapper(
            list_trips.list_trips,
        )


class ListTripsResourceWithStreamingResponse:
    def __init__(self, list_trips: ListTripsResource) -> None:
        self._list_trips = list_trips

        self.list_trips = to_streamed_response_wrapper(
            list_trips.list_trips,
        )


class AsyncListTripsResourceWithStreamingResponse:
    def __init__(self, list_trips: AsyncListTripsResource) -> None:
        self._list_trips = list_trips

        self.list_trips = async_to_streamed_response_wrapper(
            list_trips.list_trips,
        )
