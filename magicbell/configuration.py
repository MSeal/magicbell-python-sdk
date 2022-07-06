import typing

from pydantic import BaseSettings, Field

from ._version import __version__


class Configuration(BaseSettings):
    """Configuration for the Magicbell API.

    Values can be set programmatically by constructing a `Configuration` object;
    or they can be set as environment variables prefixed with `MAGICBELL_`.

    Examples
    --------
    >>> import os
    >>> from magicbell.configuration import Configuration
    >>> config = Configuration(api_key="my-api-key", api_secret="my-api-secret")
    >>> os.environ["MAGICBELL_API_KEY"] = "my-api-key"
    >>> os.environ["MAGICBELL_API_SECRET"] = "my-api-secret"
    >>> env_config = Configuration()
    >>> config == env_config
    """

    api_url: str = Field(
        "https://api.magicbell.com", description="The base URL for the Magicbell API."
    )
    api_key: typing.Optional[str] = Field(
        description="API key for the Magicbell API, sent as `X-MAGICBELL-API-KEY` header."
    )
    api_secret: typing.Optional[str] = Field(
        description="API secret for the Magicbell API, sent as `X-MAGICBELL-API-SECRET` header."
    )

    user_jwt: typing.Optional[str] = Field(
        description="A MagicBell user JWT to access protected resources such as projects.."
    )

    request_timeout_seconds: float = Field(
        5.0,
        description="The timeout for requests. "
        "An exception will be raised if the request takes longer than this.",
    )

    class Config:
        env_prefix = "magicbell_"

    def get_general_headers(
        self, idempotency_key: typing.Optional[str] = None
    ) -> typing.Dict[str, str]:
        """Return headers used for non-project related requests.

        This includes `self.api_key` as `X-MAGICBELL-API-KEY` and `self.api_secret` as `X-MAGICBELL-API-SECRET`.  # noqa: E501
        """
        headers = self.get_base_headers()
        if idempotency_key:
            headers["IDEMPOTENCY-KEY"] = idempotency_key
        if self.api_key:
            headers["X-MAGICBELL-API-KEY"] = self.api_key
        if self.api_secret:
            headers["X-MAGICBELL-API-SECRET"] = self.api_secret
        return headers

    def get_user_headers(
        self, idempotency_key: typing.Optional[str] = None
    ) -> typing.Dict[str, str]:
        """Return headers when a user JWT is required, such as projects.

        This includes `self.user_jwt` as `Authorization: Bearer <JWT>`.
        """
        headers = self.get_base_headers()
        if idempotency_key:
            headers["IDEMPOTENCY-KEY"] = idempotency_key
        if self.user_jwt:
            headers["Authorization"] = f"Bearer {self.user_jwt}"
        return headers

    def get_base_headers(self) -> typing.Dict[str, str]:
        """Return headers for all requests"""
        return {
            "User-Agent": f"magicbell-python/{__version__}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
