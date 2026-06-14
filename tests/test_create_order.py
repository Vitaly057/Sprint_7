import allure
import pytest
import requests
from config import URL_SERVICE
from data import get_order_base_payload


class TestCreateOrder:

    @allure.title('При создании заказа можно указать цвет: BLACK')
    def test_create_order_black_color_returns_track(self):
        payload = get_order_base_payload()
        payload['color'] = ['BLACK']

        response = requests.post(f'{URL_SERVICE}/api/v1/orders', json=payload)

        assert response.status_code == 201
        assert 'track' in response.json()
        assert isinstance(response.json()['track'], int)

    @allure.title('При создании заказа можно указать цвет: GREY')
    def test_create_order_grey_color_returns_track(self):
        payload = get_order_base_payload()
        payload['color'] = ['GREY']

        response = requests.post(f'{URL_SERVICE}/api/v1/orders', json=payload)

        assert response.status_code == 201
        assert 'track' in response.json()
        assert isinstance(response.json()['track'], int)

    @allure.title('При создании заказа можно указать цвет: BLACK and GREY')
    def test_create_order_black_and_grey_color_returns_track(self):
        payload = get_order_base_payload()
        payload['color'] = ['BLACK', 'GREY']

        response = requests.post(f'{URL_SERVICE}/api/v1/orders', json=payload)

        assert response.status_code == 201
        assert 'track' in response.json()
        assert isinstance(response.json()['track'], int)

    @allure.title('При создании заказа можно не указывать цвет')
    def test_create_order_no_color_returns_track(self):
        payload = get_order_base_payload()

        response = requests.post(f'{URL_SERVICE}/api/v1/orders', json=payload)

        assert response.status_code == 201
        assert 'track' in response.json()
        assert isinstance(response.json()['track'], int)
