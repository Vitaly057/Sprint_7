import allure
import pytest
import requests
from config import URL_SERVICE
from helpers.courier import generate_random_string, login_courier

class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_login_courier_valid_credentials_returns_200(self, courier):
        response = login_courier(courier['login'], courier['password'])

        assert response.status_code == 200
        assert isinstance(response.json()['id'], int)
        assert response.json()['id'] == courier['id']

    @allure.title('Для авторизации нужно передать все обязательные поля')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_login_courier_missing_field_returns_400(self, courier, missing_field):
        payload = {
            'login': courier['login'],
            'password': courier['password'],
        }
        if missing_field == 'login':
            payload.pop(missing_field)
        else:
            # API не принимает запрос без ключа password — передаём пустую строку
            payload['password'] = ''

        response = requests.post(f'{URL_SERVICE}/api/v1/courier/login', data=payload)

        assert response.status_code == 400
        assert response.json()['code'] == 400

    @allure.title('Некорректные данные для авторизации возвращают ошибку')
    @pytest.mark.parametrize(
        'login, password',
        [
            ('wrong_login', None),
            (None, 'wrong_password'),
        ],
    )
    def test_login_with_wrong_credentials_returns_404(self, courier, login, password):
        response = login_courier(
            login or courier['login'],
            password or courier['password'],
        )

        assert response.status_code == 404
        assert response.json()['code'] == 404

    @allure.title('Несуществующий пользователь не может авторизоваться')
    def test_login_nonexistent_user_returns_404(self):
        response = login_courier(
            generate_random_string(10),
            generate_random_string(10),
        )

        assert response.status_code == 404
        assert response.json()['code'] == 404
