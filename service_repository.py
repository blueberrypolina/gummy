class ServiceRepository:
    def __init__(self):
        self.services = []

    def save_service(self, service):
        self.services.append(service)

    def find_service_by_id(self, service_id):
        for service in self.services:
            if service.service_id == service_id:
                return service
        return None