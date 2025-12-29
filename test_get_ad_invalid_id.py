import requests
import pytest

BASE_URL = "https://qa-internship.avito.com"

@pytest.mark.parametrize("ad_id, expected_status", [
    ("99999999", 400),
    ("", 404),  
    ("invalid", 400),
])
def test_get_ad_invalid_id(ad_id, expected_status):
    response = requests.get(f"{BASE_URL}/api/1/item/{ad_id}")
    assert response.status_code == expected_status
