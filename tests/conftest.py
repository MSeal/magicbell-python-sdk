import httpx
import pytest

from magicbell import MagicBell
from magicbell.configuration import Configuration
from tests.mock_server import api_key, api_secret, app, user_jwt


@pytest.fixture()
def configuration():
    """A configuration object with the default values."""

    return Configuration(
        api_key=api_key,
        api_secret=api_secret,
        user_jwt=user_jwt,
    )


@pytest.fixture()
async def magicbell_client(configuration: Configuration):
    """Async HTTP client for testing the MagicBell API clients against a mock ASGI server."""

    httpx_client = httpx.AsyncClient(app=app, base_url="http://test")
    async with MagicBell(configuration=configuration, http_client=httpx_client) as mb:
        yield mb
