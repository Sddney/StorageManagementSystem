from abc import ABC, abstractmethod

class AbstractFrame(ABC):
    def __init__(self, parent):
        self.parent = parent

    @abstractmethod
    def Add(self):
        pass

    @abstractmethod
    def Delete(self):
        pass
    
    @abstractmethod
    def Show(self):
        pass

    @abstractmethod
    def Update(self):
        pass    