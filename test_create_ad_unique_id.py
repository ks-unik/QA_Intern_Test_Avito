import requests

BASE_URL = "https://qa-internship.avito.com"

def test_create_ad_unique_id():
    created_ids = [] 

    for i in range(10):  
        payload = {
            "sellerID": 100000 + i,  
            "name": f"Тестовое объявление {i+1}",
            "price": 1000 + i,
            "statistics": {
                "likes": 1,
                "viewCount": 1,
                "contacts": 1
            }
        }


        response = requests.post(f"{BASE_URL}/api/1/item", json=payload)
        print(f"Создаём объявление {i+1}, статус:", response.status_code)
        print("Ответ сервера:", response.text)


        assert response.status_code == 200


        data = response.json()
        status_text = data.get("status")
        new_id = status_text.split(" - ")[1]  # берём всё после " - "
        print("ID нового объявления:", new_id)
        assert new_id is not None, "ID нового объявления не вернулся!"


        assert new_id not in created_ids, f"ID {new_id} уже существует!"
        created_ids.append(new_id)  

    print("Все созданные ID уникальны:", created_ids)
