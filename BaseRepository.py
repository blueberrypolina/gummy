from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def find(self, query):
        pass