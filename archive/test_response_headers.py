import requests

BASE_URL = "https://qa-internship.avito.com"
SELLER_ID = 111111  

def test_response_headers():
    """
    ATC-009 — Проверка Content-Type ответа
    Метод: GET
    Ожидается: Content-Type = application/json
    """
    response = requests.get(f"{BASE_URL}/api/1/{SELLER_ID}/item")
    
    assert response.status_code == 200, f"Ожидался 200 для GET, получили {response.status_code}"
    
    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type, f"Ожидался Content-Type application/json, получили {content_type}"
