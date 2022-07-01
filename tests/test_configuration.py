import os

import pytest

from magicbell.configuration import Configuration


class TestConfiguration:
    @pytest.fixture()
    def set_config_env_vars(self):
        env_updates = {
            "MAGICBELL_API_KEY": "my-api-key",
            "MAGICBELL_API_SECRET": "my-api-secret",
            "MAGICBELL_API_URL": "https://api2.magicbell.com",
            "MAGICBELL_USER_JWT": "my-user-jwt",
            "MAGICBELL_REQUEST_TIMEOUT_SECONDS": "10.0",
        }
        original_values = {}

        for key, value in env_updates.items():
            original_values[key] = os.environ.get(key)
            os.environ[key] = value

        yield

        for key, value in original_values.items():
            if value is None:
                del os.environ[key]
            else:
                os.environ[key] = value

    @pytest.mark.usefixtures("set_config_env_vars")
    def test_configuration_can_be_loaded_from_env_vars(self):
        config = Configuration()

        assert config.api_key == "my-api-key"
        assert config.api_secret == "my-api-secret"
        assert config.api_url == "https://api2.magicbell.com"
        assert config.user_jwt == "my-user-jwt"
        assert config.request_timeout_seconds == 10.0

    def test_configuration_can_be_loaded_from_env_vars_with_missing_env_vars(self):
        config = Configuration()

        assert config.api_key is None
        assert config.api_secret is None
        assert config.api_url == "https://api.magicbell.com"
        assert config.user_jwt is None
        assert config.request_timeout_seconds == 5.0

    def test_configuration_can_be_explicitly_constructed(self):
        config = Configuration(
            api_key="my-api-key",
            api_secret="my-api-secret",
            api_url="https://api2.magicbell.com",
            user_jwt="my-user-jwt",
            request_timeout_seconds=10.0,
        )

        assert config.api_key == "my-api-key"
        assert config.api_secret == "my-api-secret"
        assert config.api_url == "https://api2.magicbell.com"
        assert config.user_jwt == "my-user-jwt"
        assert config.request_timeout_seconds == 10.0


class TestGetGeneralHeaders:
    def test_all_values_set(self):
        config = Configuration(
            api_key="my-api-key",
            api_secret="my-api-secret",
            api_url="https://api2.magicbell.com",
            user_jwt="my-user-jwt",
            request_timeout_seconds=10.0,
        )

        headers = config.get_general_headers(idempotency_key="my-idempotency-key")

        assert headers["X-MAGICBELL-API-KEY"] == "my-api-key"
        assert headers["X-MAGICBELL-API-SECRET"] == "my-api-secret"
        assert headers["IDEMPOTENCY-KEY"] == "my-idempotency-key"

        # basic headers
        assert headers["Content-Type"] == "application/json"
        assert headers["Accept"] == "application/json"
        assert "User-Agent" in headers

    def test_no_values_set(self):
        config = Configuration()
        headers = config.get_general_headers()

        assert "X-MAGICBELL-API-KEY" not in headers
        assert "X-MAGICBELL-API-SECRET" not in headers
        assert "IDEMPOTENCY-KEY" not in headers
        assert "Authorization" not in headers

        # basic headers
        assert headers["Content-Type"] == "application/json"
        assert headers["Accept"] == "application/json"
        assert "User-Agent" in headers


class TestGetUserHeaders:
    def test_all_values_set(self):
        config = Configuration(
            api_key="my-api-key",
            api_secret="my-api-secret",
            api_url="https://api2.magicbell.com",
            user_jwt="my-user-jwt",
            request_timeout_seconds=10.0,
        )

        headers = config.get_user_headers(idempotency_key="my-idempotency-key")

        assert headers["Authorization"] == "Bearer my-user-jwt"
        assert headers["IDEMPOTENCY-KEY"] == "my-idempotency-key"

        # basic headers
        assert headers["Content-Type"] == "application/json"
        assert headers["Accept"] == "application/json"
        assert "User-Agent" in headers

    def test_no_values_set(self):
        config = Configuration()
        headers = config.get_user_headers()

        assert "Authorization" not in headers

        # basic headers
        assert headers["Content-Type"] == "application/json"
        assert headers["Accept"] == "application/json"
        assert "User-Agent" in headers
