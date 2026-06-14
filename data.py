from helpers.courier import generate_random_string

METRO_STATION = 4  # Сокольники
PHONE = '+79991234567'
RENT_TIME = 5
DELIVERY_DATE = '2026-06-15'
ORDER_COMMENT = 'тестовый заказ'


def get_order_base_payload():
    return {
        'firstName': generate_random_string(8),
        'lastName': generate_random_string(8),
        'address': generate_random_string(15),
        'metroStation': METRO_STATION,
        'phone': PHONE,
        'rentTime': RENT_TIME,
        'deliveryDate': DELIVERY_DATE,
        'comment': ORDER_COMMENT,
    }
