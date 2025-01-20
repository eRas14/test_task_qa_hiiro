from locust import HttpUser, task
import locust.stats

locust.stats.PERCENTILES_TO_CHART = [0.8]
locust.stats.PERCENTILES_TO_REPORT = [0.8]
locust.stats.PERCENTILES_TO_STATISTICS = [0.8]

class TestCer80(HttpUser):

    @task()
    def create_booking(self):
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
