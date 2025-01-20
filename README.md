# Требуется:

## 1.Определить RPS при нагрузке в 10 потоков на протяжении 30 секунд

### [Отчет тестирования в формате CSV](https://github.com/eRas14/test_task_qa_hiiro/blob/main/Log_create_del_10_30sec/log_create_del_10user_30sec_report.csv)

### Код:
```
from locust import HttpUser, task

class UserTest(HttpUser):

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
        self.create_booking()

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
        self.del_booking()

    def del_booking(self): 
        url = f"https://restful-booker.herokuapp.com/booking/{self.booking_id}"
        headers = {
            'Cookie': f'token={self.token}'
        }
        self.client.delete(url, headers=headers)

   ```
### График:
![График тестирования](https://i.ibb.co/Y7kc8mF/log-create-del-10user-30sec-graph.png)

   ---
   
## 2 Определить 80-й перцентиль запроса на создание бронирования и 98-й перцентиль всех запросов при стресс тесте в 1000 потоков
### Отчет тестирования на 80-й перцентиль на создание бронирования при стресс тесте в 1000 потоков:
![График тестирования](https://i.ibb.co/hy5rC9s/per80-create-booking-1000-report.png)

### Код:
```
from locust import HttpUser, task
import locust.stats

locust.stats.PERCENTILES_TO_CHART = [0.8]
locust.stats.PERCENTILES_TO_REPORT = [0.8]
locust.stats.PERCENTILES_TO_STATISTICS = [0.8]

class TestPer80(HttpUser):

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
```

### График:
![График тестирования](https://i.ibb.co/V9v3sXH/per80-create-booking-1000-graph.png)

### Отчет тестирования на 98-й перцентиль всех запросов при стресс тесте в 1000 потоков:

### [Отчет тестирования в формате CSV](https://github.com/eRas14/test_task_qa_hiiro/blob/main/Percentile_1000/Per98/per98_log_create_del_1000_report.csv)

### Код:
```
from locust import HttpUser, task
import locust.stats

locust.stats.PERCENTILES_TO_CHART = [0.98]
locust.stats.PERCENTILES_TO_REPORT = [0.98]
locust.stats.PERCENTILES_TO_STATISTICS = [0.98]

class TestPer98(HttpUser):

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
        self.create_booking()

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
        self.del_booking()
        
    def del_booking(self): 
        url = f"https://restful-booker.herokuapp.com/booking/{self.booking_id}"
        headers = {
            'Cookie': f'token={self.token}'
        }
        self.client.delete(url, headers=headers)
```

### График:
![График тестирования](https://i.ibb.co/d5Wk2xN/per98-log-create-del-1000-graph.png)


