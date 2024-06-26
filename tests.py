from client import Client
from service import Service
from master import Master
from review import Review
from master_repository import MasterRepository
from review_repository import ReviewRepository
import unittest
from datetime import datetime
from Rules import Rules
from Appointment import Appointment


class TestRules(unittest.TestCase):

    def test_service_rating(self): #проверяем рейтинг мастера
        service1 = Service(service_id=1, name="Haircut", payment="Cash", cost=20.0)
        service2 = Service(service_id=2, name="Massage", payment="Cash", cost=20.0)
        service3 = Service(service_id=2, name="Ноготочки", payment="Card", cost=20.0)
        client = Client(client_id=1, personal_data="John Doe")
        appointment1 = Appointment(client=client, service=service1, appointment_time=datetime.now())
        appointment2 = Appointment(client=client, service=service2, appointment_time=datetime.now())
        appointment3 = Appointment(client=client, service=service3, appointment_time=datetime.now())
        master = Master(master_id=1, rating=0, address="123 Main Street")
        reviews = [
            Review(1, "Good service", 4, master=master, appointmen = appointment1),
            Review(2, "Excellent service", 5, master=master, appointmen=appointment2),
            Review(3, "Average service", 3, master=master, appointmen=appointment3)
        ]

        review_repository = ReviewRepository()
        review_repository.reviews = reviews
        master_repository = MasterRepository()
        master_repository.save_master(master)

        rules = Rules(review_repository)
        rules.service_rating(master, master_repository)

        self.assertEqual(master.rating, 4)

    def test_Service_Review(self): #1 услуга 1 отзыв

        master = Master(master_id=1, rating=0, address="123 Main Street")
        service1 = Service(service_id=1, name="Haircut", payment="Cash", cost=20.0)
        client = Client(client_id=1, personal_data="John Doe")
        appointment = Appointment(client=client, service=service1, appointment_time=datetime.now())
        appointment1 = Appointment(client=client, service=service1, appointment_time=datetime.now())
        appointment2 = Appointment(client=client, service=service1, appointment_time=datetime.now())
        appointment3 = Appointment(client=client, service=service1, appointment_time=datetime.now())
        client.appointment = [appointment]
        client.reviews =[
            Review(1, "Good service", 4, master=master, appointmen = appointment1),
            Review(2, "Excellent service", 5, master=master, appointmen=appointment2),
            Review(3, "Average service", 3, master=master, appointmen=appointment3)
        ]
        rules = Rules(None)

        self.assertFalse(rules.Service_Review(client, appointment))

    def test_OneServiceInTime(self): #нельзя записаться на две разные услуги в одно время
        service1 = Service(service_id=1, name="Haircut", payment="Cash", cost=20.0)
        service2 = Service(service_id=2, name="Massage", payment="Cash", cost=20.0)
        client = Client(client_id=1, personal_data="John Doe")
        appointment1 = Appointment(client=client, service=service1, appointment_time=datetime(2024, 3, 25, 10, 0))
        appointment2 = Appointment(client=client, service=service2, appointment_time=datetime(2024, 3, 25, 14, 0))
        client.appointment = [appointment1, appointment2]

        rules = Rules(None)

        self.assertFalse(rules.OneServiceInTime(client, service1, datetime(2024, 3, 25, 10, 0)))
        self.assertTrue(rules.OneServiceInTime(client, service1, datetime(2024, 3, 26, 10, 0)))

    def test_OnlyOneTime(self): #один временной слот одной услуги
        client = Client(client_id=1, personal_data="John Doe")
        service1 = Service(service_id=1, name="Haircut", payment="Cash", cost=20.0)
        appointment1 = Appointment(client=client, service=service1, appointment_time=datetime(2024, 3, 25, 10, 0))
        client.appointment = [appointment1]
        appointment_time1 = datetime(2024, 3, 25, 10, 0)
        appointment_time2 = datetime(2024, 3, 25, 14, 0)
        client.services_received = [service1]

        rules = Rules(None)

        self.assertFalse(rules.OnlyOneTime(appointment_time1, client))
        self.assertTrue(rules.OnlyOneTime(appointment_time2, client))

    def test_booking_successful(self):
        client = Client(1, "John Doe")
        service = Service(1, "Haircut", "cash", 50.0)
        appointment_time = datetime(2024, 3, 26, 10, 0)  # Пример времени записи
        business_logic = Rules(rew_rep=[])  # Предположим, что у вас есть класс с бизнес-логикой
        result = business_logic.booking(client, service, appointment_time)
        self.assertEqual(result, -1)

    def test_booking_same_time(self):
        client = Client(1, "John Doe")
        service1 = Service(1, "Haircut", "cash", 50.0)
        service2 = Service(2, "Massage", "card", 80.0)
        appointment_time = datetime(2024, 3, 26, 10, 0)  # Пример времени записи
        business_logic = Rules(rew_rep=[])  # Предположим, что у вас есть класс с бизнес-логикой
        business_logic.booking(client, service1, appointment_time)  # Записываем клиента на первую услугу
        result = business_logic.booking(client, service2, appointment_time)  # Пытаемся записать клиента на вторую услугу в то же время
        self.assertEqual(result, -1)

    def test_booking_same_service_same_time(self):
        client = Client(1, "John Doe")
        service = Service(1, "Haircut", "cash", 50.0)
        appointment_time1 = datetime(2024, 3, 26, 10, 0)  # Пример времени записи
        appointment_time2 = datetime(2024, 3, 26, 10, 30)  # Пример времени записи
        business_logic = Rules(rew_rep=[])  # Предположим, что у вас есть класс с бизнес-логикой
        business_logic.booking(client, service, appointment_time1)  # Записываем клиента на услугу
        result = business_logic.booking(client, service, appointment_time2)  # Пытаемся записать клиента на ту же услугу в то же время
        self.assertEqual(result, -1)




if __name__ == '__main__':
    unittest.main()
