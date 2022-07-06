import typing

from ..model.channels import WrappedChannels
from ..model.response import Response
from ._base import BaseAPI
from ._parsing import build_response


class ChannelsAPI(BaseAPI):
    async def update_channels(self, wrapped_channels: WrappedChannels) -> None:
        """Update channel configuration for a project.

        Warnings
        --------
        This method is undocumented, proceed with caution.
        """
        await self.update_channels_detailed(wrapped_channels)

    async def update_channels_detailed(
        self, wrapped_channels: WrappedChannels, idempotency_key: typing.Optional[str] = None
    ) -> Response[typing.Type[None]]:
        """Update channel configuration for a project.

        Warnings
        --------
        This method is undocumented, proceed with caution.
        """
        response = await self.client.post(
            "/channels",
            content=wrapped_channels.json(exclude_unset=True),
            headers=self.configuration.get_general_headers(idempotency_key=idempotency_key),
        )
        return build_response(response=response, out_type=None)

    async def get_channels(self) -> WrappedChannels:
        """Get channel configuration for a project.

        Warnings
        --------
        This method is undocumented, proceed with caution.
        """
        return (await self.get_channels_detailed()).parsed

    async def get_channels_detailed(self) -> Response[WrappedChannels]:
        """Get channel configuration for a project.

        Warnings
        --------
        This method is undocumented, proceed with caution.
        """
        response = await self.client.get(
            "/channels", headers=self.configuration.get_general_headers()
        )
        return build_response(response=response, out_type=WrappedChannels)
