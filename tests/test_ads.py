from config.base_test import BaseTest
import pytest
import allure

@allure.epic("Advertising")
@allure.feature("Ads Management")
@allure.story("User Flow")
class TestAds(BaseTest):

    @pytest.mark.regression
    @allure.title("Ads checks")
    def test_ads(self):
       ad = self.api_ads.create_ad()
       self.api_ads.get_ad_by_id(ad.id)
       self.api_ads.get_ads_by_sellerid(ad.sellerId)
       self.api_ads.delete_ad(ad.id)
       self.api_ads.get_statistics_1_by_id(ad.id)
       self.api_ads.get_statistics_2_by_id(ad.id)
