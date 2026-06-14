import allure
import pytest
import requests
from config import URL_SERVICE
from helpers.courier import generate_random_string


class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_valid_data_returns_201(self, created_courier):
        response, _ = created_courier

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_courier_duplicate_login_returns_409(self, registered_courier):
        duplicate_response = requests.post(
            f'{URL_SERVICE}/api/v1/courier',
            data={
                'login': registered_courier['login'],
                'password': registered_courier['password'],
                'firstName': registered_courier['firstName'],
            },
        )

        assert duplicate_response.status_code == 409
        assert duplicate_response.json()['code'] == 409

    @allure.title('Если нет обязательного поля, запрос возвращает ошибку')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_field_returns_400(self, missing_field):
        payload = {
            'login': generate_random_string(10),
            'password': generate_random_string(10),
            'firstName': generate_random_string(10),
        }
        payload.pop(missing_field)

        response = requests.post(f'{URL_SERVICE}/api/v1/courier', data=payload)

        assert response.status_code == 400
        assert response.json()['code'] == 400
