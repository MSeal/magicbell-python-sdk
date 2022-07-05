import pytest

import magicbell
from magicbell import errors


class TestCreateUser:
    async def test_error_is_handled_properly(self, magicbell_client: magicbell.MagicBell):
        with pytest.raises(errors.MagicBellHTTPClientError) as exc_info:
            await magicbell_client.users.create_user({})

        assert exc_info.value.status_code == 422

    async def test_response_is_parsed_properly(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.users.create_user(
            magicbell.WrappedUser(user=magicbell.User(email="foo@example.com"))
        )

        assert response.user.email == "foo@example.com"

    async def test_server_error_handling(self, magicbell_client: magicbell.MagicBell):
        with pytest.raises(errors.MagicBellHTTPServerError) as exc_info:
            await magicbell_client.users.create_user(
                magicbell.WrappedUser(user=magicbell.User(email="500@example.com"))
            )

        assert exc_info.value.status_code == 500


class TestUpdateUser:
    async def test_response_is_parsed_properly(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.users.update_user(
            "email:foo@example.com",
            magicbell.WrappedUser(user=magicbell.User(email="foo@example.com")),
        )

        assert response.user.email == "foo@example.com"


class TestDeleteUser:
    async def test_response_is_parsed_properly(self, magicbell_client: magicbell.MagicBell):
        await magicbell_client.users.delete_user("email:foo@example.com")


class TestDeleteUserDetailed:
    async def test_response_is_accessible(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.users.delete_user_detailed("email:foo@example.com")
        assert response.status_code == 204
