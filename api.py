from data import Api
import requests
import allure


class UserApi():

    @staticmethod
    @allure.step("Запрос на авторизацию пользователя в системе")
    def login(data):
        return requests.post(Api.USER_LOGIN, json=data, timeout=5)
    
    @staticmethod
    @allure.step("Запрос на создание нового пользователя")
    def create(data):
        return requests.post(Api.USER_CREATE, json=data, timeout=7)

class OrderApi():
    
    @staticmethod
    @allure.step("Запрос на создание заказа")
    def create(data, auth_token):
        return requests.post(Api.ORDER_CREATE, json=data, timeout=5, headers={'Authorization': f'{auth_token}'})
