import allure
import requests
from config import URL_SERVICE

class TestListOrders:

    @allure.title('При запросе списка заказов возвращается список заказов')
    def test_get_orders_list_returns_orders(self):
        response = requests.get(f'{URL_SERVICE}/api/v1/orders')

        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)
