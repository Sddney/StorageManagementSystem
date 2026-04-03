from abc import ABC, abstractmethod

class BaseItem(ABC):

    """
    Abstract base class for inventory items.
    """

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

    @abstractmethod
    def set_name(self, name):
        pass

