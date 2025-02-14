# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import list_station_list_stations_params
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
from ..types.list_station_list_stations_response import ListStationListStationsResponse

__all__ = ["ListStationsResource", "AsyncListStationsResource"]


class ListStationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListStationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Amtrak_Rohit_Divate-python#accessing-raw-response-data-eg-headers
        """
        return ListStationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListStationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Amtrak_Rohit_Divate-python#with_streaming_response
        """
        return ListStationsResourceWithStreamingResponse(self)

    def list_stations(
        self,
        *,
        coordinates: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListStationListStationsResponse:
        """
        Returns a paginated and searchable list of all train stations.

        Args:
          coordinates: The latitude and longitude of the user's location, to narrow down the search
              results to sites within a proximity of this location.

          country: Filter stations by country code

          limit: The number of items to return per page

          page: The page number to return

          search: A search term to filter the list of stations by name or address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "coordinates": coordinates,
                        "country": country,
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    list_station_list_stations_params.ListStationListStationsParams,
                ),
            ),
            cast_to=ListStationListStationsResponse,
        )


class AsyncListStationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListStationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Amtrak_Rohit_Divate-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListStationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListStationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Amtrak_Rohit_Divate-python#with_streaming_response
        """
        return AsyncListStationsResourceWithStreamingResponse(self)

    async def list_stations(
        self,
        *,
        coordinates: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListStationListStationsResponse:
        """
        Returns a paginated and searchable list of all train stations.

        Args:
          coordinates: The latitude and longitude of the user's location, to narrow down the search
              results to sites within a proximity of this location.

          country: Filter stations by country code

          limit: The number of items to return per page

          page: The page number to return

          search: A search term to filter the list of stations by name or address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "coordinates": coordinates,
                        "country": country,
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    list_station_list_stations_params.ListStationListStationsParams,
                ),
            ),
            cast_to=ListStationListStationsResponse,
        )


class ListStationsResourceWithRawResponse:
    def __init__(self, list_stations: ListStationsResource) -> None:
        self._list_stations = list_stations

        self.list_stations = to_raw_response_wrapper(
            list_stations.list_stations,
        )


class AsyncListStationsResourceWithRawResponse:
    def __init__(self, list_stations: AsyncListStationsResource) -> None:
        self._list_stations = list_stations

        self.list_stations = async_to_raw_response_wrapper(
            list_stations.list_stations,
        )


class ListStationsResourceWithStreamingResponse:
    def __init__(self, list_stations: ListStationsResource) -> None:
        self._list_stations = list_stations

        self.list_stations = to_streamed_response_wrapper(
            list_stations.list_stations,
        )


class AsyncListStationsResourceWithStreamingResponse:
    def __init__(self, list_stations: AsyncListStationsResource) -> None:
        self._list_stations = list_stations

        self.list_stations = async_to_streamed_response_wrapper(
            list_stations.list_stations,
        )
