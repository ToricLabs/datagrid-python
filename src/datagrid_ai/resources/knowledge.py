# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import knowledge_list_params, knowledge_create_params, knowledge_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.knowledge import Knowledge
from ..types.knowledge_update_response import KnowledgeUpdateResponse

__all__ = ["KnowledgeResource", "AsyncKnowledgeResource"]


class KnowledgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return KnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/datagrid-python#with_streaming_response
        """
        return KnowledgeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        files: List[FileTypes],
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Knowledge:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "files": files,
                "name": name,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/knowledge",
            body=maybe_transform(body, knowledge_create_params.KnowledgeCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    def retrieve(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Knowledge:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        return self._get(
            f"/v1/knowledge/{knowledge_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    def update(
        self,
        knowledge_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        return self._patch(
            f"/v1/knowledge/{knowledge_id}",
            body=maybe_transform({"name": name}, knowledge_update_params.KnowledgeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeUpdateResponse,
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next: str | NotGiven = NOT_GIVEN,
        sort: Literal["created_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Knowledge]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/knowledge",
            page=SyncCursorPage[Knowledge],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "next": next,
                        "sort": sort,
                    },
                    knowledge_list_params.KnowledgeListParams,
                ),
            ),
            model=Knowledge,
        )

    def delete(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/knowledge/{knowledge_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncKnowledgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/datagrid-python#with_streaming_response
        """
        return AsyncKnowledgeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        files: List[FileTypes],
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Knowledge:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "files": files,
                "name": name,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/knowledge",
            body=await async_maybe_transform(body, knowledge_create_params.KnowledgeCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    async def retrieve(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Knowledge:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        return await self._get(
            f"/v1/knowledge/{knowledge_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    async def update(
        self,
        knowledge_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        return await self._patch(
            f"/v1/knowledge/{knowledge_id}",
            body=await async_maybe_transform({"name": name}, knowledge_update_params.KnowledgeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeUpdateResponse,
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next: str | NotGiven = NOT_GIVEN,
        sort: Literal["created_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Knowledge, AsyncCursorPage[Knowledge]]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/knowledge",
            page=AsyncCursorPage[Knowledge],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "next": next,
                        "sort": sort,
                    },
                    knowledge_list_params.KnowledgeListParams,
                ),
            ),
            model=Knowledge,
        )

    async def delete(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/knowledge/{knowledge_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class KnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = to_raw_response_wrapper(
            knowledge.create,
        )
        self.retrieve = to_raw_response_wrapper(
            knowledge.retrieve,
        )
        self.update = to_raw_response_wrapper(
            knowledge.update,
        )
        self.list = to_raw_response_wrapper(
            knowledge.list,
        )
        self.delete = to_raw_response_wrapper(
            knowledge.delete,
        )


class AsyncKnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = async_to_raw_response_wrapper(
            knowledge.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            knowledge.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            knowledge.update,
        )
        self.list = async_to_raw_response_wrapper(
            knowledge.list,
        )
        self.delete = async_to_raw_response_wrapper(
            knowledge.delete,
        )


class KnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = to_streamed_response_wrapper(
            knowledge.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            knowledge.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            knowledge.update,
        )
        self.list = to_streamed_response_wrapper(
            knowledge.list,
        )
        self.delete = to_streamed_response_wrapper(
            knowledge.delete,
        )


class AsyncKnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = async_to_streamed_response_wrapper(
            knowledge.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            knowledge.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            knowledge.update,
        )
        self.list = async_to_streamed_response_wrapper(
            knowledge.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            knowledge.delete,
        )