from utils.helper import Helper
from services.ads.endpoints import Endpoints
from services.ads.payloads import Payloads
import requests
from services.ads.models.ad_model import AdModel, ModelStatistic
import allure
import re

class AdsAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()

    def attach_step_status(self, step_name: str, status_code: int):
        print(f"[STEP] {step_name} — статус код {status_code}")
        with allure.step(f"{step_name} — статус код {status_code}"):
            pass

    @allure.step("Create ad")
    def create_ad(self):
        response = requests.post(url=self.endpoints.create_ad, json=self.payloads.create_ad)
        
        response_data = response.json()
        assert response.status_code == 200, response_data

        uuid_match = re.search(
            r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', 
            response_data["status"], 
            re.I
        )
        
        assert uuid_match, f"UUID не найден в ответе: {response_data}"
        uuid = uuid_match.group()

        ad_response = requests.get(url=self.endpoints.get_ad_by_id(uuid))
        
        ad_data = ad_response.json()
        assert ad_response.status_code == 200, ad_data

        ad_item = ad_data[0]

        self.attach_response(ad_item)
        model = AdModel(**ad_item)
        self.attach_step_status("Create ad — формат и данные корректны", 200)
        return model

    @allure.step("Get ad by ID")
    def get_ad_by_id(self, uuid):
        response = requests.get(url=self.endpoints.get_ad_by_id(uuid))
        response_data = response.json()
        assert response.status_code == 200, response_data

        ad_item = response_data[0]

        self.attach_response(ad_item)
        model = AdModel(**ad_item)
        self.attach_step_status("Get ad by ID — выполнено успешно", 200)
        return model
    
    @allure.step("Get ads by sellerId")
    def get_ads_by_sellerid(self, sellerId):
        response = requests.get(url=self.endpoints.get_ads_by_sellerid(sellerId))
        response_data = response.json()
        assert response.status_code == 200, response_data

        ad_item = response_data[0]

        self.attach_response(ad_item)
        model = AdModel(**ad_item)
        self.attach_step_status("Get ads by sellerId — выполнено успешно", 200)
        return model
    
    @allure.step("Delete ad")
    def delete_ad(self, id):
        response = requests.delete(url=self.endpoints.delete_ad(id))
        assert response.status_code == 200, f"Delete failed with status: {response.status_code}"
        self.attach_step_status("Delete ad — выполнено успешно", 200)
        
        self.attach_response({
        "status_code": response.status_code,
        "message": "Ad deleted successfully"
    })
        
    @allure.step("Get statistic by id")
    def get_statistics_1_by_id(self, id):
        response = requests.get(url=self.endpoints.get_statistics_1_by_id(id))
        response_data = response.json()
        assert response.status_code == 200, response_data

        ad_item = response_data[0]

        self.attach_response(ad_item)
        model = ModelStatistic(**ad_item)
        self.attach_step_status("Get statistic (/api/1/) by id — выполнено успешно", 200)
        return model
    
    def get_statistics_2_by_id(self, id):
        response = requests.get(url=self.endpoints.get_statistics_2_by_id(id))
        response_data = response.json()
        assert response.status_code == 200, response_data

        ad_item = response_data[0]

        self.attach_response(ad_item)
        model = ModelStatistic(**ad_item)
        self.attach_step_status("Get statistic (/api/2/) by id — выполнено успешно", 200)
        return model