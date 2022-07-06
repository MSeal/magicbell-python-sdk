import typing

import httpx


class BaseMagicBellError(Exception):
    """Base class for all MagicBell errors."""

    pass


class MagicBellConfigurationError(BaseMagicBellError):
    """Raised when there is an error in the configuration."""

    pass


class BaseMagicBellHTTPError(BaseMagicBellError):
    """Base class for all MagicBell HTTP errors."""

    def __init__(self, response: httpx.Response):
        """Create a new MagicBell HTTP error.

        Parameters
        ----------
        response : httpx.Response
            The HTTP response that caused the error.
        """

        self.response = response

    def __str__(self):
        error_lines = [
            f"({self.response.status_code})",
            f"Reason: {self.response.reason_phrase}",
        ]
        if self.response.headers:
            error_lines.append(f"HTTP response headers: {self.response.headers}")
        if self.response.content:
            error_lines.append(f"HTTP response body: {self.response.text}")
        return "\n".join(error_lines)

    @property
    def status_code(self) -> int:
        return self.response.status_code

    @property
    def content(self) -> bytes:
        return self.response.content

    def json(self) -> typing.Any:
        return self.response.json()


class MagicBellHTTPError(BaseMagicBellHTTPError):
    """Unknown/unhandled HTTP errors."""

    pass


class MagicBellHTTPClientError(MagicBellHTTPError):
    """HTTP client errors (400-499)."""

    pass


class MagicBellHTTPServerError(MagicBellHTTPError):
    """HTTP server errors (500-599)."""

    pass
