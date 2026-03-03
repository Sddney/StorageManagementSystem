from sqlite3 import *
from abc import ABC, abstractmethod

class DatabaseMethods(ABC):
    @abstractmethod
    def get(self, id):
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
