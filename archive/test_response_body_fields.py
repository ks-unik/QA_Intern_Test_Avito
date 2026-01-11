import requests

BASE_URL = "https://qa-internship.avito.com"
SELLER_ID = 111111  
ADS_ENDPOINT = f"/api/1/{SELLER_ID}/item"

def test_response_body_fields():
    response_get = requests.get(f"{BASE_URL}{ADS_ENDPOINT}")
    assert response_get.status_code == 200, f"Ожидался 200, получили {response_get.status_code}"
    
    data = response_get.json()
    assert isinstance(data, list), "Ожидался список объявлений"
    
    for ad in data:
        assert "id" in ad, "Отсутствует поле 'id'"
        assert "sellerId" in ad, "Отсутствует поле 'sellerId'"
        assert "name" in ad, "Отсутствует поле 'name'"
        assert "price" in ad, "Отсутствует поле 'price'"
        assert "statistics" in ad, "Отсутствует поле 'statistics'"
