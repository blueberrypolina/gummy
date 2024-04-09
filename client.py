class Client:
    def __init__(self, client_id, personal_data):
        self.id = client_id
        self.personal_data = personal_data
        self.appointment = []
        self.masters = []
        self.reviews = []

    def __eq__(self, other):
        if isinstance(other, Client):
            return (
                        self.id == other.id and
                        self.personal_data == other.personal_data and
                        self.masters == other.masters and
                        self.reviews == other.reviews)
        return False
