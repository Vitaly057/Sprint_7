import random
import string

import requests

from config import URL_SERVICE


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def register_new_courier_and_return_login_password():
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        'login': login,
        'password': password,
        'firstName': first_name,
    }

    response = requests.post(f'{URL_SERVICE}/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def create_courier(login=None, password=None, first_name=None):
    payload = {
        'login': login or generate_random_string(10),
        'password': password or generate_random_string(10),
        'firstName': first_name or generate_random_string(10),
    }
    response = requests.post(f'{URL_SERVICE}/api/v1/courier', data=payload)
    return response, payload


def login_courier(login, password):
    payload = {
        'login': login,
        'password': password,
    }
    return requests.post(f'{URL_SERVICE}/api/v1/courier/login', data=payload)


def delete_courier(courier_id):
    return requests.delete(f'{URL_SERVICE}/api/v1/courier/{courier_id}')
