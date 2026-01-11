import requests
import re

BASE_URL = "https://qa-internship.avito.com"

def test_create_ad_valid_data():

    payload = {
        "sellerID": 123,
        "name": "Тестовое объявление",
        "price": 1000,
        "statistics": {
            "likes": 1,
            "viewCount": 1,
            "contacts": 1
        }
    }


    response = requests.post(f"{BASE_URL}/api/1/item", json=payload)
    

    print("Status code:", response.status_code)
    print("Response body:", response.text)
    assert response.status_code == 200, "Запрос вернул ошибку"


    data = response.json()
    status_string = data["status"]  


    ad_id = status_string.split(" - ")[1]
    print("Extracted ad ID:", ad_id)

    
    assert re.match(r"^[0-9a-fA-F-]{36}$", ad_id), "ID не похож на UUID"

    
