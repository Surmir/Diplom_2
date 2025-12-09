import allure
import pytest
from api import OrderApi
from data import OrderData
from data import OrderResponse as correct_r


class TestApiOrder():

    @allure.title("Успешное создание заказа с авторизацией и ингредиентами")
    def test_create_order_auth_user_with_ingr_success(self, token_user):
        token = token_user
        r = OrderApi.create(OrderData.PAYLOAD_CORRECT, token)
        assert r.status_code == correct_r.CODE_SUCCESS_CREATE and r.json()["name"] == correct_r.BODY_SUCCESS_CREATE

    @allure.title("Появляеться ошибка при создании заказа с авторизацией и без ингредиентов")
    def test_create_order_auth_user_without_ingr_error(self, token_user):
        token = token_user
        r = OrderApi.create(OrderData.PAYLOAD_EMPTY, token)
        assert r.status_code == correct_r.CODE_ERROR_EMPTY and r.json()["message"] == correct_r.BODY_ERROR_EMPTY

    @allure.title("Появляеться ошибка при создании заказа с авторизацией и неверным хешем ингредиентов")
    def test_create_order_auth_user_wrong_hesh_ingr_error(self, token_user):
        token = token_user
        r = OrderApi.create(OrderData.PAYLOAD_INCORRECT, token)
        assert r.status_code == correct_r.CODE_ERROR_INCORRECT

    @allure.title("Появляеться ошибка при создании заказа без авторизации и с ингредиентами")
    def test_create_order_not_auth_user_with_ingr_error(self):
        token = ""
        r = OrderApi.create(OrderData.PAYLOAD_CORRECT, token)
        assert r.status_code == correct_r.CODE_ERROR_NOT_AUTH and r.json()["message"] == correct_r.BODY_ERROR_NOT_AUTH
