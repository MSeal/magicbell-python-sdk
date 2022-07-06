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


class TestGetChannels:
    async def test_response_is_parsed(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.channels.get_channels()
        email_channel = response.channels[0]

        assert len(response.channels) == 6
        assert email_channel.slug == "email"
        assert email_channel.configuration.providers["mailgun"]["enabled"] is True
        assert email_channel.configuration.providers["mailgun"]["api_key"] == "1234"
        assert email_channel.configuration.providers["mailgun"]["sender_domain"] == "example.com"
        assert (
            email_channel.configuration.providers["mailgun"]["from"]["email"]
            == "notification@example.com"
        )
        assert email_channel.configuration.providers["mailgun"]["from"]["name"] == "Example"
