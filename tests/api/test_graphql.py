import magicbell


class TestQuery:
    async def test_response_is_parsed(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.graphql.query(
            "query test($foo: String){ logs(foo: $foo) { id } }", variables={"foo": "bar"}
        )
        assert response is not None


class TestQueryDetailed:
    async def test_response_can_be_accessed(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.graphql.query_detailed(
            "query test($foo: String){ logs(foo: $foo) { id } }", variables={"foo": "bar"}
        )
        assert response.status_code == 200
        assert response.json_content() is not None


class TestUserQuery:
    async def test_response_is_parsed(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.graphql.user_query(
            "query { notifications { id }}", user_hmac="hmac_123", user_external_id="123"
        )
        assert response is not None


class TestUserQueryDetailed:
    async def test_response_can_be_accessed(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.graphql.user_query_detailed(
            "query { notifications { id }}", user_hmac="hmac_123", user_external_id="123"
        )
        assert response.status_code == 200
        assert response.json_content() is not None
