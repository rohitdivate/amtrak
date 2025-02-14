# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from Amtrak_Rohit_Divate import Amtrak, AsyncAmtrak
from Amtrak_Rohit_Divate.types import ListStationListStationsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestListStations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_stations(self, client: Amtrak) -> None:
        list_station = client.list_stations.list_stations()
        assert_matches_type(ListStationListStationsResponse, list_station, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_stations_with_all_params(self, client: Amtrak) -> None:
        list_station = client.list_stations.list_stations(
            coordinates="coordinates",
            country="country",
            limit=1,
            page=1,
            search="Milano Centrale",
        )
        assert_matches_type(ListStationListStationsResponse, list_station, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_stations(self, client: Amtrak) -> None:
        response = client.list_stations.with_raw_response.list_stations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_station = response.parse()
        assert_matches_type(ListStationListStationsResponse, list_station, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_stations(self, client: Amtrak) -> None:
        with client.list_stations.with_streaming_response.list_stations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_station = response.parse()
            assert_matches_type(ListStationListStationsResponse, list_station, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncListStations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_stations(self, async_client: AsyncAmtrak) -> None:
        list_station = await async_client.list_stations.list_stations()
        assert_matches_type(ListStationListStationsResponse, list_station, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_stations_with_all_params(self, async_client: AsyncAmtrak) -> None:
        list_station = await async_client.list_stations.list_stations(
            coordinates="coordinates",
            country="country",
            limit=1,
            page=1,
            search="Milano Centrale",
        )
        assert_matches_type(ListStationListStationsResponse, list_station, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_stations(self, async_client: AsyncAmtrak) -> None:
        response = await async_client.list_stations.with_raw_response.list_stations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_station = await response.parse()
        assert_matches_type(ListStationListStationsResponse, list_station, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_stations(self, async_client: AsyncAmtrak) -> None:
        async with async_client.list_stations.with_streaming_response.list_stations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_station = await response.parse()
            assert_matches_type(ListStationListStationsResponse, list_station, path=["response"])

        assert cast(Any, response.is_closed) is True
