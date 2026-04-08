from sqlite3 import *
from abc import ABC, abstractmethod

class DatabaseMethods(ABC):
    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def insert(self, item):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def update(self, id, item):
        pass

    @abstractmethod
    def get_all(self):
        pass
