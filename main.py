from xmlReposirory import XMLRepository
from client import Client
from service import Service
from Rules import Rules
import datetime


def save_to_xml(client_data):
    repository = XMLRepository("base.xml")
    repository.save(client_data)


def deleteService(id):
    rep = XMLRepository("base.xml")
    rep.deleteservice_instance(id)


def find_clients_by_name(name):
    client_repository = XMLRepository("base.xml")
    clients = client_repository.findClient(name)
    return clients


def find_service_by_name(name):
    service_repository = XMLRepository("base.xml")
    service = service_repository.findService(name)
    return service


def UseBooking(client_name, service_name):
    users = find_clients_by_name(client_name)
    services = find_service_by_name(service_name)
    client = Client(client_id=users[0]["id"], personal_data=users[0]["personal_data"])
    date = datetime.date(2024, 5, 7)
    service = Service(id=services[0]["id"], name=services[0]["name"], payment=services[0]["payment"],
                      cost=services[0]["cost"])
    rules = Rules()
    a = rules.booking(client=client, service=service, date=date)
    deleteService(client.id)
    save_to_xml(client)
    return a


if __name__ == "__main__":
    b = UseBooking("John Doe", "Haircut")
    print(b)
