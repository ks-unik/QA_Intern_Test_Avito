import requests

BASE_URL = "https://qa-internship.avito.com"
ADS_ENDPOINT = "/ads"

def test_get_ads_no_ads():
    """
    ATC-007 — Получение списка объявлений продавца без объявлений
    Ожидается: пустой список или 404, если нет объявлений
    """
    seller_id_without_ads = 123456 

    response = requests.get(
        f"{BASE_URL}{ADS_ENDPOINT}",
        params={"sellerId": seller_id_without_ads}
    )

    assert response.status_code in (200, 404), "Ожидался статус код 200 или 404"

    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, list), "Ожидался список"
        assert len(data) == 0, "Ожидался пустой список объявлений"
    else:
        # 404 — корректно, объявлений нет
        pass
