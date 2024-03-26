from client import Client
from service import Service
from master import Master
from review import Review
from client_repository import ClientRepository
from service_repository import ServiceRepository
from master_repository import MasterRepository
from review_repository import ReviewRepository

# Создаем фейковые репозитории
client_repository = ClientRepository()
service_repository = ServiceRepository()
master_repository = MasterRepository()
review_repository = ReviewRepository()

# Пример использования
client1 = Client(client_id=1, personal_data="John Doe")
client_repository.save_client(client1)

service1 = Service(service_id=1, name="Haircut", payment="Card", cost=30)
service_repository.save_service(service1)

master1 = Master(master_id=1, rating=4.5,  address="123 Main St")
master_repository.save_master(master1)

review1 = Review(review_id=1, text="Great service!", rating=5)
client1.reviews.append(review1)
review_repository.save_review(review1)

# Пример получения данных из репозиториев
retrieved_client = client_repository.find_client_by_id(1)
retrieved_service = service_repository.find_service_by_id(1)
retrieved_master = master_repository.find_master_by_id(1)
retrieved_review = review_repository.find_review_by_id(1)

# Выводим информацию
print(f"Client: {retrieved_client.personal_data}")
print(f"Service: {retrieved_service.name}, Cost: {retrieved_service.cost}")
print(f"Master: Rating: {retrieved_master.rating}, Time: {retrieved_master.appointment_time}, Address: {retrieved_master.address}")
print(f"Review: {retrieved_review.text}, Rating: {retrieved_review.rating}")