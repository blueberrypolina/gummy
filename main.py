from xmlReposirory import XMLRepository
from client import Client
from service import Service
from Rules import Rules
import datetime


def save_to_xml(user_data):
    repository = XMLRepository("base.xml")
    repository.save(user_data)


def deleteVacs(id):
    rep = XMLRepository("base.xml")
    rep.deletevacancy_instance(id)


def find_users_by_name(name):
    user_repository = XMLRepository("base.xml")
    users = user_repository.findClient(name)
    return users


def find_vacs_by_name(name):
    vacs_repository = XMLRepository("base.xml")
    vacs = vacs_repository.findService(name)
    return vacs


def UseBooking(user_name, service_name):
    users = find_users_by_name(user_name)
    services = find_vacs_by_name(service_name)
    client = Client(client_id=users[0]["id"], personal_data=users[0]["personal_data"])
    date = datetime.date(2024, 5, 7)
    service = Service(id=services[0]["id"], name=services[0]["name"], payment=services[0]["payment"],
                      cost=services[0]["cost"])
    rules = Rules()
    a = rules.booking(client=client, service=service, date=date)
    deleteVacs(client.id)
    save_to_xml(client)
    return a


if __name__ == "__main__":
    b = UseBooking("John Doe", "Haircut")
    print(b)
