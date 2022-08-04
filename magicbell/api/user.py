import typing

from ..model.response import Response
from ..model.user import WrappedUser
from ._base import BaseAPI
from ._parsing import build_request_content, build_response


class UserAPI(BaseAPI):
    async def create_user(
        self,
        wrapped_user: typing.Union[WrappedUser, typing.Dict],
        idempotency_key: typing.Optional[str] = None,
    ) -> WrappedUser:
        """Create a user, returning a `WrappedUser`.
        Please note that you must provide the user's email or the external id so MagicBell can uniquely identify the user.
        The external id, if provided, must be unique to the user.
        """
        return (await self.create_user_detailed(wrapped_user, idempotency_key)).parsed

    async def create_user_detailed(
        self,
        wrapped_user: typing.Union[WrappedUser, typing.Dict],
        idempotency_key: typing.Optional[str] = None,
    ) -> Response[WrappedUser]:
        """Create a user, returning a `Response`.
        Please note that you must provide the user's email or the external id so MagicBell can uniquely identify the user.
        The external id, if provided, must be unique to the user.
        """
        response = await self.client.post(
            "/users",
            headers=self.configuration.get_general_headers(idempotency_key=idempotency_key),
            content=build_request_content(wrapped_user),
        )
        return build_response(response=response, out_type=WrappedUser)

    async def update_user(
        self,
        user_id: str,
        wrapped_user: typing.Union[WrappedUser, typing.Dict],
        idempotency_key: typing.Optional[str] = None,
    ) -> WrappedUser:
        """Update a user by id, email or external_id, returning a `WrappedUser`.
        The user id is the MagicBell user id.
        Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id.
        """
        return (await self.update_user_detailed(user_id, wrapped_user, idempotency_key)).parsed

    async def update_user_detailed(
        self,
        user_id: str,
        wrapped_user: typing.Union[WrappedUser, typing.Dict],
        idempotency_key: typing.Optional[str] = None,
    ) -> Response[WrappedUser]:
        """Update a user by id, email or external_id, returning a `Response`.
        The user id is the MagicBell user id.
        Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id.
        """
        url = f"/users/{user_id}"
        response = await self.client.put(
            url,
            headers=self.configuration.get_general_headers(idempotency_key=idempotency_key),
            content=build_request_content(wrapped_user),
        )
        return build_response(response=response, out_type=WrappedUser)

    async def delete_user(self, user_id: str, idempotency_key: typing.Optional[str] = None) -> None:
        """Delete a user by id, email or external_id.
        The user id is the MagicBell user id.
        Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id.
        We will delete the user completely 7 days after.
        If the user makes a request to the API, the deletion will be canceled.
        This will happen when the notification inbox for this user is loaded in your app, for example.
        """
        await self.delete_user_detailed(user_id, idempotency_key)

    async def delete_user_detailed(
        self, user_id: str, idempotency_key: typing.Optional[str] = None
    ) -> Response[typing.Type[None]]:
        """Delete a user by id, email or external_id, returning a `Response`.
        The user id is the MagicBell user id.
        Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id.
        We will delete the user completely 7 days after.
        If the user makes a request to the API, the deletion will be canceled.
        This will happen when the notification inbox for this user is loaded in your app, for example.
        """
        url = f"/users/{user_id}"
        response = await self.client.delete(
            url, headers=self.configuration.get_general_headers(idempotency_key=idempotency_key)
        )
        return build_response(response=response, out_type=None)
