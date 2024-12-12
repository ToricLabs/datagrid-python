# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid.types import Knowledge, KnowledgeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        knowledge = client.knowledge.create(
            files=[b"raw file contents"],
        )
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        knowledge = client.knowledge.create(
            files=[b"raw file contents"],
            name="name",
        )
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.knowledge.with_raw_response.create(
            files=[b"raw file contents"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.knowledge.with_streaming_response.create(
            files=[b"raw file contents"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Knowledge, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        knowledge = client.knowledge.list()
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        knowledge = client.knowledge.list(
            direction="asc",
            limit=0,
            next="next",
            sort="created_at",
        )
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.knowledge.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.knowledge.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowledge:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.create(
            files=[b"raw file contents"],
        )
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.create(
            files=[b"raw file contents"],
            name="name",
        )
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.knowledge.with_raw_response.create(
            files=[b"raw file contents"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.knowledge.with_streaming_response.create(
            files=[b"raw file contents"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Knowledge, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.list()
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.list(
            direction="asc",
            limit=0,
            next="next",
            sort="created_at",
        )
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.knowledge.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.knowledge.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(KnowledgeListResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True
