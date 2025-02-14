# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from Amtrak_Rohit_Divate import Amtrak, AsyncAmtrak
from Amtrak_Rohit_Divate.types import (
    BookingPayResponse,
    BookingListResponse,
    BookingCreateResponse,
    BookingRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBookings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Amtrak) -> None:
        booking = client.bookings.create()
        assert_matches_type(BookingCreateResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Amtrak) -> None:
        booking = client.bookings.create(
            has_bicycle=True,
            has_dog=True,
            passenger_name="John Doe",
            trip_id="4f4e4e1-c824-4d63-b37a-d8d698862f1d",
        )
        assert_matches_type(BookingCreateResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Amtrak) -> None:
        response = client.bookings.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = response.parse()
        assert_matches_type(BookingCreateResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Amtrak) -> None:
        with client.bookings.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = response.parse()
            assert_matches_type(BookingCreateResponse, booking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Amtrak) -> None:
        booking = client.bookings.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BookingRetrieveResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Amtrak) -> None:
        response = client.bookings.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = response.parse()
        assert_matches_type(BookingRetrieveResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Amtrak) -> None:
        with client.bookings.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = response.parse()
            assert_matches_type(BookingRetrieveResponse, booking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Amtrak) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `booking_id` but received ''"):
            client.bookings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Amtrak) -> None:
        booking = client.bookings.list()
        assert_matches_type(BookingListResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Amtrak) -> None:
        booking = client.bookings.list(
            limit=1,
            page=1,
        )
        assert_matches_type(BookingListResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Amtrak) -> None:
        response = client.bookings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = response.parse()
        assert_matches_type(BookingListResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Amtrak) -> None:
        with client.bookings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = response.parse()
            assert_matches_type(BookingListResponse, booking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Amtrak) -> None:
        booking = client.bookings.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert booking is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Amtrak) -> None:
        response = client.bookings.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = response.parse()
        assert booking is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Amtrak) -> None:
        with client.bookings.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = response.parse()
            assert booking is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Amtrak) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `booking_id` but received ''"):
            client.bookings.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_pay(self, client: Amtrak) -> None:
        booking = client.bookings.pay(
            booking_id="1725ff48-ab45-4bb5-9d02-88745177dedb",
        )
        assert_matches_type(BookingPayResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_pay_with_all_params(self, client: Amtrak) -> None:
        booking = client.bookings.pay(
            booking_id="1725ff48-ab45-4bb5-9d02-88745177dedb",
            amount=49.99,
            currency="bam",
            source={
                "address_country": "gb",
                "cvc": "123",
                "exp_month": 12,
                "exp_year": 2025,
                "name": "J. Doe",
                "number": "4242424242424242",
                "address_city": "London",
                "address_line1": "123 Fake Street",
                "address_line2": "4th Floor",
                "address_post_code": "N12 9XX",
                "object": "card",
            },
        )
        assert_matches_type(BookingPayResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_pay(self, client: Amtrak) -> None:
        response = client.bookings.with_raw_response.pay(
            booking_id="1725ff48-ab45-4bb5-9d02-88745177dedb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = response.parse()
        assert_matches_type(BookingPayResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_pay(self, client: Amtrak) -> None:
        with client.bookings.with_streaming_response.pay(
            booking_id="1725ff48-ab45-4bb5-9d02-88745177dedb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = response.parse()
            assert_matches_type(BookingPayResponse, booking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_pay(self, client: Amtrak) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `booking_id` but received ''"):
            client.bookings.with_raw_response.pay(
                booking_id="",
            )


class TestAsyncBookings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAmtrak) -> None:
        booking = await async_client.bookings.create()
        assert_matches_type(BookingCreateResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAmtrak) -> None:
        booking = await async_client.bookings.create(
            has_bicycle=True,
            has_dog=True,
            passenger_name="John Doe",
            trip_id="4f4e4e1-c824-4d63-b37a-d8d698862f1d",
        )
        assert_matches_type(BookingCreateResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAmtrak) -> None:
        response = await async_client.bookings.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = await response.parse()
        assert_matches_type(BookingCreateResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAmtrak) -> None:
        async with async_client.bookings.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = await response.parse()
            assert_matches_type(BookingCreateResponse, booking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAmtrak) -> None:
        booking = await async_client.bookings.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BookingRetrieveResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAmtrak) -> None:
        response = await async_client.bookings.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = await response.parse()
        assert_matches_type(BookingRetrieveResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAmtrak) -> None:
        async with async_client.bookings.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = await response.parse()
            assert_matches_type(BookingRetrieveResponse, booking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAmtrak) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `booking_id` but received ''"):
            await async_client.bookings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAmtrak) -> None:
        booking = await async_client.bookings.list()
        assert_matches_type(BookingListResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAmtrak) -> None:
        booking = await async_client.bookings.list(
            limit=1,
            page=1,
        )
        assert_matches_type(BookingListResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAmtrak) -> None:
        response = await async_client.bookings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = await response.parse()
        assert_matches_type(BookingListResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAmtrak) -> None:
        async with async_client.bookings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = await response.parse()
            assert_matches_type(BookingListResponse, booking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAmtrak) -> None:
        booking = await async_client.bookings.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert booking is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAmtrak) -> None:
        response = await async_client.bookings.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = await response.parse()
        assert booking is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAmtrak) -> None:
        async with async_client.bookings.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = await response.parse()
            assert booking is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAmtrak) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `booking_id` but received ''"):
            await async_client.bookings.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_pay(self, async_client: AsyncAmtrak) -> None:
        booking = await async_client.bookings.pay(
            booking_id="1725ff48-ab45-4bb5-9d02-88745177dedb",
        )
        assert_matches_type(BookingPayResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_pay_with_all_params(self, async_client: AsyncAmtrak) -> None:
        booking = await async_client.bookings.pay(
            booking_id="1725ff48-ab45-4bb5-9d02-88745177dedb",
            amount=49.99,
            currency="bam",
            source={
                "address_country": "gb",
                "cvc": "123",
                "exp_month": 12,
                "exp_year": 2025,
                "name": "J. Doe",
                "number": "4242424242424242",
                "address_city": "London",
                "address_line1": "123 Fake Street",
                "address_line2": "4th Floor",
                "address_post_code": "N12 9XX",
                "object": "card",
            },
        )
        assert_matches_type(BookingPayResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_pay(self, async_client: AsyncAmtrak) -> None:
        response = await async_client.bookings.with_raw_response.pay(
            booking_id="1725ff48-ab45-4bb5-9d02-88745177dedb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        booking = await response.parse()
        assert_matches_type(BookingPayResponse, booking, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_pay(self, async_client: AsyncAmtrak) -> None:
        async with async_client.bookings.with_streaming_response.pay(
            booking_id="1725ff48-ab45-4bb5-9d02-88745177dedb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            booking = await response.parse()
            assert_matches_type(BookingPayResponse, booking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_pay(self, async_client: AsyncAmtrak) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `booking_id` but received ''"):
            await async_client.bookings.with_raw_response.pay(
                booking_id="",
            )
