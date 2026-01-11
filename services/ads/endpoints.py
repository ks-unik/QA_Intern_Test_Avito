
HOST = "https://qa-internship.avito.com"

class Endpoints:

    create_ad = f"{HOST}/api/1/item"
    get_ad_by_id = lambda self, id: f"{HOST}/api/1/item/{id}"
    get_ads_by_sellerid = lambda self, sellerid: f"{HOST}/api/1/{sellerid}/item"
    delete_ad = lambda self, id: f"{HOST}/api/2/item/{id}"
    get_statistics_1_by_id = lambda self, id: f"{HOST}/api/1/statistic/{id}"
    get_statistics_2_by_id = lambda self, id: f"{HOST}/api/2/statistic/{id}"