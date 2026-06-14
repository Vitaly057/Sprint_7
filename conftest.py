import pytest

from helpers.courier import (
    create_courier,
    delete_courier,
    login_courier,
    register_new_courier_and_return_login_password,
)


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


@pytest.fixture
def created_courier():
    response, payload = create_courier()
    yield response, payload

    login_response = login_courier(payload['login'], payload['password'])
    delete_courier(login_response.json()['id'])


@pytest.fixture
def registered_courier():
    _, payload = create_courier()
    yield payload

    login_response = login_courier(payload['login'], payload['password'])
    delete_courier(login_response.json()['id'])
