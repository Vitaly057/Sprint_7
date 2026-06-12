import pytest

from helpers.courier import delete_courier, login_courier, register_new_courier_and_return_login_password


@pytest.fixture
def courier():
    login, password, first_name = register_new_courier_and_return_login_password()
    login_response = login_courier(login, password)
    courier_id = login_response.json()['id']

    yield {
        'login': login,
        'password': password,
        'firstName': first_name,
        'id': courier_id,
    }

    delete_courier(courier_id)
