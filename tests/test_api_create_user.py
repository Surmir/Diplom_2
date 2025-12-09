import allure
import pytest
from api import UserApi
from helpers import HelperUser
from data import UserData
from data import UserCreateResponse as correct_r


class TestApiCreateUser():

    @allure.title("Проверка создания уникального пользователя")
    @allure.description("Создается новый пользователь если все даннные валидны, обязательные поля заполнены")
    def test_create_user_success(self):
        r = UserApi.create(HelperUser.PAYLOAD_REGISTR)
        assert r.status_code == correct_r.CODE_SUCCESS and correct_r.BODY_SUCCESS in r.json()["accessToken"]

    @allure.title("Проверка создания пользователя, который уже зарегистрирован")
    @allure.description("При создании пользователя с уже существующим логином появляется ошибка")
    def test_create_user_already_registered_error(self):
        r = UserApi.create(UserData.REGISTRED_USER_DATA)
        assert r.status_code == correct_r.CODE_ERROR_SAME_LOGIN and r.json()["message"] == correct_r.BODY_ERROR_SAME_LOGIN
        
    @allure.title("Проверка создания пользователя, без email, password or name")
    @allure.description("При создании пользователя появляется ошибка, если одного из обязательных полей нет")
    @pytest.mark.parametrize('data', HelperUser.TEST_CREATE_USER)
    def test_create_user_empty_field_error(self, data):
        data = data
        r = UserApi.create(data)
        assert r.status_code == correct_r.CODE_ERROR_EMPTY_FIELD and r.json()["message"] == correct_r.BODY_ERROR_EMPTY_FIELD
