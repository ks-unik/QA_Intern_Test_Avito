import requests

BASE_URL = "https://qa-internship.avito.com"

def test_create_ad_invalid_data():

    payload = {
        "sellerID": "не число",  
        "name": "",              
        "price": -100,           
        "statistics": {
            "likes": -1,         
            "viewCount": 0,
            "contacts": 0
        }
    }

    response = requests.post(f"{BASE_URL}/api/1/item", json=payload)

    print("Status code:", response.status_code)
    print("Response body:", response.text)


    assert response.status_code == 400


    data = response.json()
    assert "result" in data
    assert "message" in data["result"]
