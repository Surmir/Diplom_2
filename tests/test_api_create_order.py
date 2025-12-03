import allure
import pytest
from api import OrderApi
from data import OrderData
from data import OrderResponse as correct_r


class TestApiOrder():

    @allure.title("Проверка создания заказа с авторизацией")
    @allure.description("Проверка создания заказа с авторизацией и ингредиентами")
    def test_create_order_auth_user_success(self, token_user):
        token = token_user
        r = OrderApi.create(OrderData.PAYLOAD_CORRECT, token)
        assert r.status_code == correct_r.CODE_SUCCESS_CREATE and r.json()["name"] == correct_r.BODY_SUCCESS_CREATE

    @allure.title("Проверка создания заказа с авторизацией")
    @allure.description("Проверка появления ошибки при создании заказа с авторизацией и телом запроса {ingredient}")
    @pytest.mark.parametrize('ingredient, code, body', OrderData.TEST_ORDER_ERROR)
    def test_create_order_wrong_body_error(self, token_user, ingredient, code, body):
        token = token_user
        r = OrderApi.create(ingredient, token)
        assert r.status_code == code and r.json()["message"] == body

    @allure.title("Проверка создания заказа без авторизации")
    @allure.description("Проверка появления ошибки при создании заказа без авторизации")
    def test_create_order_not_auth_user_error(self):
        token = ""
        r = OrderApi.create(OrderData.PAYLOAD_CORRECT, token)
        assert r.status_code == correct_r.CODE_ERROR_NOT_AUTH and r.json()["message"] == correct_r.BODY_ERROR_NOT_AUTH
