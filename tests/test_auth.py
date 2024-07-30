import requests
from faker import Faker
import pytest
URL='https://restful-booker.herokuapp.com'
fake=Faker()

class TestAuth:
    def test_auth_with_valid_data(self):
        body = {"username": "admin", "password": "password123"}
        response = requests.post(url=f'{URL}/auth', json=body)
        assert response.status_code == 200 and "token" in response.text
        print (response.text)


    @pytest.mark.skip(reason="it accepts auth with invalid username data types")
    @pytest.mark.parametrize("username", [123, False])
    def test_auth_with_invalid_username(self, username):
        body={"username": username, "password": fake.password()}
        response = requests.post(url=f'{URL}/auth', json=body)
        assert response.status_code == 400

    @pytest.mark.skip(reason="it accepts auth with invalid password data types")
    @pytest.mark.parametrize("password", [123, False])
    def test_auth_with_invalid_password(self, password):
        body={"username": fake.email(), "password": password}
        response = requests.post(url=f'{URL}/auth', json=body)
        assert response.status_code == 400

    @pytest.mark.skip(reason="it accepts auth with empty username")
    def test_auth_with_empty_username(self):
        body = {"username": None, "password": fake.password()}
        response = requests.post(url=f'{URL}/auth', json=body)
        assert response.status_code == 400

    @pytest.mark.skip(reason="it accepts auth with empty password")
    def test_auth_with_empty_password(self):
        body = {"username": fake.email(), "password": None}
        response = requests.post(url=f'{URL}/auth', json=body)
        assert response.status_code == 400
