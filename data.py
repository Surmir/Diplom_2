from urls import Url


class UserData():

    REGISTRED_USER_DATA = {
                            "email": "greog@yandex.ru",
                            "password": "576567rt",
                            "name": "falcon"
                            }

    PAYLOAD_LOGIN = {
                    "email": REGISTRED_USER_DATA["email"],
                    "password": REGISTRED_USER_DATA["password"]
                    }

    TEST_WRONG_DATA_LOGIN = [
                            {"email": "error12@yandex.ru",
                            "password": REGISTRED_USER_DATA["password"]},
                            {"email": REGISTRED_USER_DATA["email"],
                            "password": "error12"}
                            ]

class Api():

    url = Url.STELLAR_BURGER

    USER_LOGIN = f"{url}/api/auth/login"
    USER_CREATE = f"{url}/api/auth/register"
    ORDER_CREATE = f"{url}/api/orders"

class OrderData():

    PAYLOAD_CORRECT = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]}
    
    PAYLOAD_INCORRECT = {"ingredients": ["error5a71d1f82001bd0006d","error5a71d1f82001bd0006f"]}
    
    PAYLOAD_EMPTY = {"ingredients": []}

class UserCreateResponse():

    CODE_SUCCESS = 200
    BODY_SUCCESS = "Bearer"

    CODE_ERROR_SAME_LOGIN = 403
    BODY_ERROR_SAME_LOGIN = "User already exists"

    CODE_ERROR_EMPTY_FIELD = 403
    BODY_ERROR_EMPTY_FIELD = "Email, password and name are required fields"

class UserLoginResponse():

    CODE_SUCCESS = 200
    BODY_SUCCESS = "Bearer"

    CODE_ERROR_WRONG_DATA = 401
    BODY_ERROR_WRONG_DATA = "email or password are incorrect"

class OrderResponse():

    CODE_SUCCESS_CREATE = 200
    BODY_SUCCESS_CREATE = "Флюоресцентный бессмертный бургер"

    CODE_ERROR_NOT_AUTH = 401
    BODY_ERROR_NOT_AUTH = "You shold be authorised"

    CODE_ERROR_INCORRECT = 500

    CODE_ERROR_EMPTY = 400
    BODY_ERROR_EMPTY = "Ingredient ids must be provided"
