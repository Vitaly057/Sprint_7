import allure
import pytest
import requests
from config import URL_SERVICE
from helpers.courier import generate_random_string

class TestCreateOrder:

    @allure.title('При создании заказа можно указать цвет: {color}')
    @pytest.mark.parametrize(
        'color',
        [
            pytest.param(['BLACK'], id='BLACK'),
            pytest.param(['GREY'], id='GREY'),
            pytest.param(['BLACK', 'GREY'], id='BLACK and GREY'),
            pytest.param(None, id='no color'),
        ],
    )
    def test_create_order_with_color_returns_track(self, color):
        payload = {
            'firstName': generate_random_string(8),
            'lastName': generate_random_string(8),
            'address': generate_random_string(15),
            'metroStation': 4,  # Сокольники
            'phone': '+79991234567',
            'rentTime': 5,
            'deliveryDate': '2026-06-15',
            'comment': 'тестовый заказ',
        }
        if color is not None:
            payload['color'] = color

        response = requests.post(f'{URL_SERVICE}/api/v1/orders', json=payload)

        assert response.status_code == 201
        assert 'track' in response.json()
        assert isinstance(response.json()['track'], int)
