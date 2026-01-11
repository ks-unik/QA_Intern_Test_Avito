import requests
import re

BASE_URL = "https://qa-internship.avito.com"

def test_get_ads_existing_seller_with_ads():
    seller_id = 123456
    created_ids = []

    for i in range(3):
        payload = {
            "sellerID": seller_id,
            "name": f"Объявление {i+1} для seller {seller_id}",
            "price": 1000 + i,
            "statistics": {
                "likes": 1,
                "viewCount": 1,
                "contacts": 1
            }
        }
        response = requests.post(f"{BASE_URL}/api/1/item", json=payload)
        assert response.status_code == 200, f"POST failed: {response.text}"
        
        json_resp = response.json()
        status_text = json_resp.get("status")
        # достаем UUID из текста
        ad_id_match = re.search(r"([0-9a-fA-F-]{36})", status_text)
        assert ad_id_match, f"POST response has no id: {json_resp}"
        ad_id = ad_id_match.group(1)
        created_ids.append(ad_id)

    get_resp = requests.get(f"{BASE_URL}/api/1/{seller_id}/item")
    assert get_resp.status_code == 200, f"GET failed: {get_resp.text}"

    ads = get_resp.json()

    returned_ids = [ad["id"] for ad in ads]
    for ad_id in created_ids:
        assert ad_id in returned_ids, f"Ad {ad_id} not returned"


    for ad_id in created_ids:
        del_resp = requests.delete(f"{BASE_URL}/api/2/item/{ad_id}")
        assert del_resp.status_code == 200, f"DELETE failed: {del_resp.text}"

