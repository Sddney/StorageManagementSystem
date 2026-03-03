from abc import ABC, abstractmethod

class BaseItem(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_name():
        pass
    
    @abstractmethod
    def get_id(self):
        pass

