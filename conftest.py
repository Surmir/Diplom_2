import pytest
from data import UserData
from api import UserApi


@pytest.fixture
def token_user():
    payload = UserData.PAYLOAD_LOGIN
    login = UserApi.login(payload)
    token = login.json()["accessToken"]
    return token
