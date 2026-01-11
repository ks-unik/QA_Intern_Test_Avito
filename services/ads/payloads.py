from faker import Faker
import random
from datetime import date, timedelta

fake = Faker('ru_RU')

class Payloads:

    create_ad = {
        "sellerId": random.randint(111_111, 999_999),
        "name": fake.sentence(nb_words=3).rstrip("."),
        "price": random.randint(1, 100_000),
        "statistics": {"likes": 1, "viewCount": 1, "contacts": 1},
    }