import pytest

import magicbell
from magicbell import errors


class TestCreateNotification:
    @pytest.mark.parametrize("body", [{}, {"notification": {}}])
    async def test_validation_error_is_handled_properly(
        self, magicbell_client: magicbell.MagicBell, body: dict
    ):
        with pytest.raises(errors.MagicBellHTTPClientError) as exc_info:
            await magicbell_client.realtime.create_notification(body)

        assert exc_info.value.status_code == 422

    async def test_response_is_parsed(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.realtime.create_notification(
            magicbell.WrappedNotification(
                notification=magicbell.Notification(
                    title="Test notification",
                    recipients=[magicbell.Recipient(email="foo@bar.com")],
                    overrides=magicbell.NotificationOverrides(
                        providers=magicbell.NotificationProvidersOverrides(
                            mailgun={"template": "test-template"}
                        )
                    ),
                )
            )
        )

        assert isinstance(response, magicbell.WrappedCreatedNotificationBroadcast)
        assert response.notification.id is not None
