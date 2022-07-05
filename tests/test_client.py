"""Tests for the MagicBell client.

The tests in this file aren't meant to be exhaustive over all the API endpoints, but rather to
ensure that the client handles expected responses as well as errors correctly.
"""
import pytest

import magicbell
from magicbell import errors
from magicbell.configuration import Configuration


class TestAuthenticationErrorHandling:
    @pytest.fixture(autouse=True)
    def clear_configuration(self, configuration: Configuration):
        configuration.api_key = None
        configuration.api_secret = None
        configuration.user_jwt = None

    async def test_when_api_key_isnt_sent_error_is_handled(
        self, magicbell_client: magicbell.MagicBell
    ):
        with pytest.raises(errors.MagicBellHTTPClientError) as exc_info:
            await magicbell_client.realtime.create_notification(
                magicbell.WrappedNotification(
                    notification=magicbell.Notification(
                        title="Test",
                        recipients=[magicbell.Recipient(email="test@example.com")],
                    )
                )
            )

        assert exc_info.value.status_code == 403
        assert exc_info.value.json()["errors"][0]["code"] == "api_key_not_provided"

    async def test_when_api_secret_isnt_sent_error_is_handled(
        self, magicbell_client: magicbell.MagicBell, configuration: Configuration
    ):
        configuration.api_key = "my-api-key"

        with pytest.raises(errors.MagicBellHTTPClientError) as exc_info:
            await magicbell_client.realtime.create_notification(
                magicbell.WrappedNotification(
                    notification=magicbell.Notification(
                        title="Test",
                        recipients=[magicbell.Recipient(email="test@example.com")],
                    )
                )
            )

        assert exc_info.value.status_code == 403
        assert exc_info.value.json()["errors"][0]["code"] == "api_secret_not_provided"

    async def test_when_user_jwt_isnt_sent_error_is_handled(
        self, magicbell_client: magicbell.MagicBell
    ):
        with pytest.raises(errors.MagicBellHTTPClientError) as exc_info:
            await magicbell_client.projects.list_projects(42)

        assert exc_info.value.status_code == 403
        assert exc_info.value.json()["errors"][0]["code"] == "forbidden"
