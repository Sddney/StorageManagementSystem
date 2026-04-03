from sqlite3 import *
from abc import ABC, abstractmethod

class DatabaseMethods(ABC):

    """
    Abstract base class for database operations.
    """
    @abstractmethod
    def get_one(self, id):  #retrieve a single record by its id
        pass
    
    @abstractmethod
    def insert(self, item):   #insert a new record into the database.
        pass
    
    @abstractmethod
    def delete(self, id):  #remove the record with the given id from the database.
        pass

    @abstractmethod
    def update(self, id, item):  #overwrite an existing record with the data from item.
        pass
    
    @abstractmethod
    def get_all(self):  #retrieve every record from the table.
        pass
