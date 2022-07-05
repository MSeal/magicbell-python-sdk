import typing

from ..model.notification import WrappedCreatedNotificationBroadcast, WrappedNotification
from ..model.response import Response
from ._base import BaseAPI
from ._parsing import build_request_content, build_response


class RealtimeAPI(BaseAPI):
    """APIs to manage notifications in real-time"""

    async def create_notification(
        self,
        wrapped_notification: typing.Union[WrappedNotification, typing.Dict],
        idempotency_key: typing.Optional[str] = None,
    ) -> WrappedCreatedNotificationBroadcast:
        """Send a notification to one or multiple users, returning a `Notification`.
        Specify `idempotency_key` to prevent duplicate notifications.
        https://www.magicbell.com/docs/rest-api/idempotent-requests
        """
        return (
            await self.create_notification_detailed(wrapped_notification, idempotency_key)
        ).parsed

    async def create_notification_detailed(
        self,
        wrapped_notification: typing.Union[WrappedNotification, typing.Dict],
        idempotency_key: typing.Optional[str] = None,
    ) -> Response[WrappedCreatedNotificationBroadcast]:
        """Send a notification to one or multiple users, returning a `Response`.
        Specify `idempotency_key` to prevent duplicate notifications.
        https://www.magicbell.com/docs/rest-api/idempotent-requests
        """
        response = await self.client.post(
            "/notifications",
            headers=self.configuration.get_general_headers(idempotency_key=idempotency_key),
            content=build_request_content(wrapped_notification),
        )
        return build_response(response=response, out_type=WrappedCreatedNotificationBroadcast)
