import typing

import httpx

from magicbell import errors
from magicbell.model import Response, ResponseBodyT


def check_response(response: httpx.Response) -> None:
    if response.is_client_error:
        raise errors.MagicBellHTTPClientError(response)
    elif response.is_server_error:
        raise errors.MagicBellHTTPServerError(response)
    elif not response.is_success:
        raise errors.MagicBellHTTPError(response)


def build_response(
    *, response: httpx.Response, out_type: typing.Optional[typing.Type[ResponseBodyT]]
) -> Response[ResponseBodyT]:
    check_response(response)

    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=out_type.parse_raw(response.content) if out_type else None,
    )
