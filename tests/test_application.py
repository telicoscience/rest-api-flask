import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "userssds",
            "last_name": "ascd",
            "cpf": "992.839.520-90",
            "email": "john.doe@dacszzd.om",
            "birth_date": "1990-01-01"
         }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "userssds",
            "last_name": "ascd",
            "cpf": "992.839.520-92",
            "email": "john.doe@dacszzd.om",
            "birth_date": "1990-01-01"
         }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(serlf, client, invalid_user):
        response = client.post("/user", json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data
