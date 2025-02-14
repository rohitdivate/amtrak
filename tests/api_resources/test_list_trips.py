# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from Amtrak_Rohit_Divate import AmtrakRohitDivate, AsyncAmtrakRohitDivate
from Amtrak_Rohit_Divate.types import ListTripListTripsResponse
from Amtrak_Rohit_Divate._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestListTrips:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_trips(self, client: AmtrakRohitDivate) -> None:
        list_trip = client.list_trips.list_trips(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListTripListTripsResponse, list_trip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_trips_with_all_params(self, client: AmtrakRohitDivate) -> None:
        list_trip = client.list_trips.list_trips(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            bicycles=True,
            dogs=True,
            limit=1,
            page=1,
        )
        assert_matches_type(ListTripListTripsResponse, list_trip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_trips(self, client: AmtrakRohitDivate) -> None:
        response = client.list_trips.with_raw_response.list_trips(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_trip = response.parse()
        assert_matches_type(ListTripListTripsResponse, list_trip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_trips(self, client: AmtrakRohitDivate) -> None:
        with client.list_trips.with_streaming_response.list_trips(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_trip = response.parse()
            assert_matches_type(ListTripListTripsResponse, list_trip, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncListTrips:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_trips(self, async_client: AsyncAmtrakRohitDivate) -> None:
        list_trip = await async_client.list_trips.list_trips(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListTripListTripsResponse, list_trip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_trips_with_all_params(self, async_client: AsyncAmtrakRohitDivate) -> None:
        list_trip = await async_client.list_trips.list_trips(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            bicycles=True,
            dogs=True,
            limit=1,
            page=1,
        )
        assert_matches_type(ListTripListTripsResponse, list_trip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_trips(self, async_client: AsyncAmtrakRohitDivate) -> None:
        response = await async_client.list_trips.with_raw_response.list_trips(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_trip = await response.parse()
        assert_matches_type(ListTripListTripsResponse, list_trip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_trips(self, async_client: AsyncAmtrakRohitDivate) -> None:
        async with async_client.list_trips.with_streaming_response.list_trips(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            origin="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_trip = await response.parse()
            assert_matches_type(ListTripListTripsResponse, list_trip, path=["response"])

        assert cast(Any, response.is_closed) is True
