from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from SQLRepository import SQLAlchemyRepository

# Импортируем модели и репозитории из соответствующих модулей
from sqlConfig import Base, ClientModel, MasterModel, AppointmentModel, ServiceModel
from Rules import Rules



# Настройка SQLAlchemy
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
sql_rep = SQLAlchemyRepository(session)

# Создание начальных данных
def create_initial_data(rep:SQLAlchemyRepository):
    # Создание мастера
    master = MasterModel(id=1, rating=4.5, address="123 Main St")
    rep.save(master)

    # Создание клиента
    client = ClientModel(id=1, personal_data="John Doe")
    rep.save(client)

    # Создание сервиса
    service = ServiceModel(id=1, name="Haircut", payment="Cash", cost=20.0)
    rep.save(service)


def UseBooking(client_name, service_name):
    client = sql_rep.find(ClientModel, {"personal_data": client_name})
    service = sql_rep.find(ServiceModel, {"name": service_name})

    if client and service:
        rules = Rules(session)
        date = datetime.datetime(2024, 5, 7, 10, 0)  # Задаем конкретное время для теста
        result = rules.booking(client, service, date)

        appointment = AppointmentModel(client_id=client.id, service_id=service.id, appointment_time=date)
        client.appointments.append(appointment)
        sql_rep.save(appointment)
        return result
    return -1


if __name__ == "__main__":
    # Создание начальных данных
    create_initial_data(sql_rep)

    # Вызов метода UseBooking
    result = UseBooking("John Doe", "Haircut")
    print("Booking result:", result)
