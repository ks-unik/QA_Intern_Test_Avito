import requests

BASE_URL = "https://qa-internship.avito.com"

def test_get_ad_existing_id():
    # 1. Создаём тестовое объявление через POST
    payload = {
        "sellerID": 123456,
        "name": "Объявление для GET",
        "price": 1000,
        "statistics": {
            "likes": 1,
            "viewCount": 1,
            "contacts": 1
        }
    }

    create_resp = requests.post(f"{BASE_URL}/api/1/item", json=payload)
    assert create_resp.status_code == 200


    ad_id = create_resp.json()["status"].split(" - ")[1]


    get_resp = requests.get(f"{BASE_URL}/api/1/item/{ad_id}")
    assert get_resp.status_code == 200


    data = get_resp.json()[0]  


    assert data["id"] == ad_id
    assert data["name"] == payload["name"]
    assert data["price"] == payload["price"]
    assert data["statistics"] == payload["statistics"]
