import httpx

from magicbell.configuration import Configuration


class BaseAPI:
    def __init__(self, client: httpx.AsyncClient, configuration: Configuration) -> None:
        self.client = client
        self.configuration = configuration
