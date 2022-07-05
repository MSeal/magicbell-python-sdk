import magicbell

test_channels = magicbell.WrappedChannels(
    channels=[
        magicbell.Channel(
            slug="email",
            configuration=magicbell.ChannelConfiguration(
                providers={
                    "mailgun": {
                        "enabled": True,
                        "api_key": "api_key",
                        "sender_domain": "email.example.com",
                    }
                }
            ),
        )
    ]
)


class TestUpdateChannels:
    async def test_channels_can_be_updated(self, magicbell_client: magicbell.MagicBell):
        await magicbell_client.channels.update_channels(wrapped_channels=test_channels)


class TestUpdateChannelsDetailed:
    async def test_response_can_be_accessed(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.channels.update_channels_detailed(
            wrapped_channels=test_channels
        )

        assert response.status_code == 204
