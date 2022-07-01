import typing

import httpx

from .api import ProjectAPI, RealtimeAPI, UserAPI
from .configuration import Configuration


class MagicBell:
    """Central class for interacting with the MagicBell API.
    To be used as an asynchronous context manager.

    Examples
    --------
    >>> async with MagicBell() as mb:
    >>>    projects = (await mb.projects.list_projects()).projects
    >>>    for project in projects:
    >>>        print(project.id, project.name, project.api_key)
    >>> # OR: use an explicit config
    >>> async with MagicBell(Configuration(api_key="my-api-key", api_secret="my-secret")) as mb:
    >>>    ...
    """

    configuration: Configuration
    http_client: httpx.AsyncClient
    projects: ProjectAPI
    realtime: RealtimeAPI

    def __init__(self, configuration: typing.Optional[Configuration] = None):
        """Create a new MagicBell instance.

        Parameters
        ----------
        configuration : Configuration, optional
            Configuration to use for the API.
            If not provided, a default configuration will be used.
            The default configuration will try to load configuration from environment variables using the `MAGICBELL_` prefix.  # noqa: E501
        """

        self.configuration = configuration or Configuration()
        self.http_client = httpx.AsyncClient(
            base_url=self.configuration.api_url,
            timeout=httpx.Timeout(timeout=self.configuration.request_timeout_seconds),
        )

        self.projects = ProjectAPI(self.http_client, self.configuration)
        self.realtime = RealtimeAPI(self.http_client, self.configuration)
        self.users = UserAPI(self.http_client, self.configuration)

    async def __aenter__(self):
        await self.http_client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.http_client.__aexit__(exc_type, exc_val, exc_tb)
