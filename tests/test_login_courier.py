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

    @allure.title('Для авторизации нужно передать логин')
    def test_login_courier_missing_login_returns_400(self, courier):
        payload = {
            'password': courier['password'],
        }

        response = requests.post(f'{URL_SERVICE}/api/v1/courier/login', data=payload)

        assert response.status_code == 400
        assert response.json()['code'] == 400

    @allure.title('Для авторизации нужно передать пароль')
    def test_login_courier_missing_password_returns_400(self, courier):
        payload = {
            'login': courier['login'],
            'password': '',
        }

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
