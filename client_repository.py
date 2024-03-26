class ClientRepository:
    def __init__(self):
        self.clients = []

    def save_client(self, client):
        self.clients.append(client)

    def find_client_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None