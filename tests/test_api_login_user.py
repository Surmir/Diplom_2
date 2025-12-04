import allure
import pytest
from api import UserApi
from data import UserData
from data import UserLoginResponse as correct_r


class TestApiUserLogin():

    @allure.title("Проверка авторизации пользователя под существующим пользователем")
    @allure.description("Пользователь авторизуется если поля email и password " \
    "заполнены данными существующего пользователя")
    def test_user_login_success(self):
        r = UserApi.login(UserData.PAYLOAD_LOGIN)
        assert r.status_code == correct_r.CODE_SUCCESS and correct_r.BODY_SUCCESS in r.json()["accessToken"]

    @allure.title("Проверка авторизации пользователя, с неверным логином или паролем")
    @allure.description("При авторизации пользователя с неверным логином или паролем появляется ошибка")
    @pytest.mark.parametrize('data', UserData.TEST_WRONG_DATA_LOGIN)
    def test_user_login_wrong_data_error(self, data):
        r = UserApi.login(data)
        assert r.status_code == correct_r.CODE_ERROR_WRONG_DATA and r.json()["message"] == correct_r.BODY_ERROR_WRONG_DATA
