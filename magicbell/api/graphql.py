import typing

from ..errors import MagicBellConfigurationError
from ..model import Response
from ._base import BaseAPI
from ._parsing import build_response


class GraphQLAPI(BaseAPI):
    """Perform GraphQL queries and mutations against the MagicBell GraphQL API.
    https://www.magicbell.com/docs/graphql-api/overview
    """

    async def query(
        self, query: str, variables: typing.Optional[typing.Dict] = None
    ) -> typing.Dict:
        """Query the GraphQL API, sends the X-MAGICBELL-API-KEY and X-MAGICBELL-SECRET-KEY headers.

        Use `user_query` if you want to send the X-MAGICBELL-API-KEY and X-MAGICBELL-USER-HMAC headers.
        """
        return (await self.query_detailed(query=query, variables=variables)).json_content()

    async def query_detailed(
        self, query: str, variables: typing.Optional[typing.Dict] = None
    ) -> Response[typing.Type[None]]:
        """Query the GraphQL API, sends the X-MAGICBELL-API-KEY and X-MAGICBELL-SECRET-KEY headers.

        Use `user_query` if you want to send the X-MAGICBELL-API-KEY and X-MAGICBELL-USER-HMAC headers.
        """
        return await self._query(
            headers=self.configuration.get_general_headers(), query=query, variables=variables
        )

    async def user_query(
        self,
        query: str,
        user_hmac: str,
        user_external_id: typing.Optional[str] = None,
        user_email: typing.Optional[str] = None,
        variables: typing.Optional[typing.Dict] = None,
    ) -> typing.Dict:
        """Query the GraphQL API as a user, sends the X-MAGICBELL-API-KEY and X-MAGICBELL-USER-HMAC headers.
        Must specify either `user_external_id` or `user_email`.
        """
        return (
            await self.user_query_detailed(
                query=query,
                user_hmac=user_hmac,
                user_external_id=user_external_id,
                user_email=user_email,
                variables=variables,
            )
        ).json_content()

    async def user_query_detailed(
        self,
        query: str,
        user_hmac: str,
        user_external_id: typing.Optional[str] = None,
        user_email: typing.Optional[str] = None,
        variables: typing.Optional[typing.Dict] = None,
    ) -> Response[typing.Type[None]]:
        """Query the GraphQL API as a user, sends the X-MAGICBELL-API-KEY and X-MAGICBELL-USER-HMAC headers.
        Must specify either `user_external_id` or `user_email`.
        """
        if not user_external_id and not user_email:
            raise MagicBellConfigurationError(
                "Either user_external_id or user_email must be provided"
            )

        headers = {
            "X-MAGICBELL-USER-HMAC": user_hmac,
            "X-MAGICBELL-API-KEY": self.configuration.api_key,
            **self.configuration.get_base_headers(),
        }
        if user_external_id:
            headers["X-MAGICBELL-USER-EXTERNAL-ID"] = user_external_id
        if user_email:
            headers["X-MAGICBELL-USER-EMAIL"] = user_email

        return await self._query(headers=headers, query=query, variables=variables)

    async def _query(
        self,
        headers: typing.Dict[str, str],
        query: str,
        variables: typing.Optional[typing.Dict] = None,
    ) -> Response:
        """Query the GraphQL API."""
        response = await self.client.post(
            "/graphql",
            json={"query": query, "variables": variables},
            headers=headers,
        )
        return build_response(response=response, out_type=None)
