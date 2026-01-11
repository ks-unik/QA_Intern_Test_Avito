import requests

BASE_URL = "https://qa-internship.avito.com"
ADS_ENDPOINT = "/ads"

def test_get_ads_invalid_seller():
    """
    ATC-008 — Получение объявлений с невалидным sellerId
    Ожидается: 404 Not Found для всех невалидных sellerId
    """

    response_empty = requests.get(
        f"{BASE_URL}{ADS_ENDPOINT}",
        params={"sellerId": ""}
    )
    assert response_empty.status_code == 404, "Ожидался статус код 404 для пустого sellerId"

    response_out_of_range = requests.get(
        f"{BASE_URL}{ADS_ENDPOINT}",
        params={"sellerId": 9999999}
    )
    assert response_out_of_range.status_code == 404, "Ожидался статус код 404 для sellerId вне диапазона"
