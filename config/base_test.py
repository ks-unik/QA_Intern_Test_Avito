from services.ads.api_ads import AdsAPI

class BaseTest:

    def setup_method(self):
        self.api_ads = AdsAPI()