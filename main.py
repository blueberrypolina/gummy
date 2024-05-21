from JSONRepository import JsonRepository
from client import Client
from master import Master
from review import Review
from service import Service
from Appointment import Appointment
from Rules import Rules
import datetime

repository = JsonRepository('data')  # директория, куда будут сохраняться файлы


def find_client_by_name(name):
    def query(obj):
        if isinstance(obj, Client):
            return obj.personal_data == name
        return False

    return query


def find_service_by_name(name):
    def query(obj):
        if isinstance(obj, Service):
            return obj.name == name
        return False

    return query


# Создание объектов
client = Client(1, "John Doe")
client1 = Client(2, "Вова Камушкин")
master = Master(1, 4, "123 Main St")
service = Service(1, "Haircut", "Cash", 20.0)

# Сохранение объектов
repository.save(client)
repository.save(client1)
repository.save(master)
repository.save(service)
date = datetime.datetime(2024, 5, 7, 10, 0)
rules = Rules()

if rules.booking(client, service, date) == 1:
    appointment = Appointment(1, client=client, service=service, appointment_time=date)
    client.appointment.append(appointment.id)
    repository.delete_client_by_id(client.id)
    repository.save(client)
    print("Всё ок")
else:
    print("Что-то не так...")
