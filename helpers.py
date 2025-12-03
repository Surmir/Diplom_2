import random
import string


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

class HelperUser():
      
        PAYLOAD_REGISTR = {
                        "email": f"{generate_random_string(8)}@yandex.ru",
                        "password": generate_random_string(7),
                        "name": generate_random_string(7)
                        }
      
        TEST_CREATE_USER = [
                        {"email": "",
                        "password": PAYLOAD_REGISTR["password"],
                        "name": PAYLOAD_REGISTR["name"]},
                        {"email": PAYLOAD_REGISTR["email"],
                        "password": "",
                        "name": PAYLOAD_REGISTR["name"]},
                        {"email": PAYLOAD_REGISTR["email"],
                        "password": PAYLOAD_REGISTR["password"],
                        "name": ""}
                        ]
