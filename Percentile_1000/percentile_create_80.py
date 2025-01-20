from locust import HttpUser, task
import locust.stats

locust.stats.PERCENTILES_TO_CHART = [0.8]
locust.stats.PERCENTILES_TO_REPORT = [0.8]
locust.stats.PERCENTILES_TO_STATISTICS = [0.8]

class WelcomeToRestfulBookerTest(HttpUser):
    token = None #для хранения токена
    booking_id = None #для хранения букинг_ид

    @task()
    def login_user(self):
        url = "https://restful-booker.herokuapp.com/auth"
        token_data= {
            "username": "admin",
            "password": "password123"
        }
        response = self.client.post(url, json=token_data)
        self.token = response.json().get("token")
        self.add_booking()

    def add_booking(self):
        url = "https://restful-booker.herokuapp.com/booking"
        booking_data= {
            "firstname" : "Aibek",
            "lastname" : "Urazov",
            "totalprice" : 322,
            "depositpaid" : True,
            "bookingdates" : {
            "checkin" : "2025-01-19",
            "checkout" : "2025-01-20"
    },
    "additionalneeds" : "free_wifi"
        }
        response = self.client.post(url, json=booking_data)
        self.booking_id = response.json().get("bookingid") 
 