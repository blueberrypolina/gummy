import os
import json
from review import Review
from master import Master
from BaseRepository import BaseRepository  # предположим, что у тебя есть файл base_repository.py с базовым репозиторием


class JsonRepository(BaseRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return {}

    def save(self, obj):
        class_name = obj.__class__.__name__
        obj_id = obj.id
        obj_data = obj.__dict__

        if class_name not in self.data:
            self.data[class_name] = {}

        if obj_id in self.data[class_name]:
            print(f"Object with id {obj_id} already exists in class {class_name}. Skipping...")
            return

        if obj_id not in self.data[class_name]:
            self.data[class_name][obj_id] = {"data": obj_data}

        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def find(self, query):
        result = []

        for class_name, class_data in self.data.items():
            module = __import__(class_name)
            class_ = getattr(module, class_name)

            for obj_id, obj_info in class_data.items():
                obj_data = obj_info['data']
                obj = class_(**obj_data)

                # Добавляем объект в результат, если он удовлетворяет запросу
                if query(obj):
                    result.append(obj)

        return result

    def delete_client_by_id(self, client_id):
        if "Client" not in self.data or client_id not in self.data["Client"]:
            print(f"Client with ID {client_id} not found. Skipping deletion.")
            return

        del self.data["Client"][client_id]

        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)
