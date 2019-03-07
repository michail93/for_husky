from django.test import TestCase

# Create your tests here.
from.models import FirstMaster, SecondMaster, ThirdMaster
from datetime import datetime


# Тесты
class CarRepairShopTestCase(TestCase):
    def setUp(self):
        self.user1 = FirstMaster.objects.create(name="TestUser1", surname="TestUser1", patronymic="TestUser1",
                                              auto_mark="TestCar1", register_date=datetime.strptime("2019-04-10T12:30",
                                                                                                    "%Y-%m-%dT%H:%M"))
        self.user2 = FirstMaster.objects.create(name="TestUser2", surname="TestUser2", patronymic="TestUser2",
                                            auto_mark="TestCar2", register_date=datetime.strptime("2019-04-10T14:00",
                                                                                                  "%Y-%m-%dT%H:%M"))

    def test_simple(self):
        self.assertEqual(1,1, "NOT EQUAL!")

    def test_user1(self):
        self.assertEquals(self.user1.register_date.weekday(), 2)

    def test_day_off(self):
        response = self.client.post("/carshop/register/", data={
                "surname": "TestUser3",
                "name": "TestUser3",
                "patronymic": "TestUser3",
                "auto_mark": "TestCar3",
                "date_time": "2019-04-13T13:15",
                "master": "1"
            }, content_type="application/json")
        self.assertEquals(response.json()["response"], "warning", "test_day_off was failed!")

    def test_time_off_one(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "2019-04-10T09:30",
            "master": "2"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_time_off_one was failed!")

    def test_time_off_two(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "2019-04-10T19:30",
            "master": "3"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_time_off_two was failed!")

    def test_filled_form(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "2019-04-10T11:30"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_filled_form was failed!")

    def test_valid_date_time(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "123456THello:30",
            "master": "2"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_valid_date_time was failed!")

    def test_past_time(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "2019-02-10T10:30",
            "master": "3"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_past_time was failed!")

    def test_number_of_master_one(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "2019-04-10T10:30",
            "master": "1a"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_number_of_master_one was failed!")

    def test_number_of_master_two(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "2019-04-10T10:30",
            "master": "5"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_number_of_master_two was failed!")

    def test_busy_time_one(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "2019-04-10T11:40",
            "master": "1"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_busy_time_one was failed!")

    def test_busy_time_two(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "2019-04-10T13:35",
            "master": "1"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_busy_time_two was failed!")

    def test_busy_time_three(self):
        response = self.client.post("/carshop/register/", data={
            "surname": "TestUser3",
            "name": "TestUser3",
            "patronymic": "TestUser3",
            "auto_mark": "TestCar3",
            "date_time": "2019-04-10T14:55",
            "master": "1"
        }, content_type="application/json")
        self.assertEqual(response.json()["response"], "warning", "test_busy_time_two was failed!")
















