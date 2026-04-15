from abc import ABC, abstractmethod

class AbstractFrame(ABC):
    """
    Abstract base class for GUI frames.
    Ensures all GUI classes implement required methods.
    """
    def __init__(self, parent):  #store a reference to the parent Tkinter widget.
        self.parent = parent

    @abstractmethod
    def add(self):  #render a form for creating a new record.
        pass

    @abstractmethod
    def delete(self):  #render a form for deleting an existing record by ID.
        pass
    
    @abstractmethod
    def show(self):  #render a table view of all records.
        pass

    @abstractmethod
    def update(self):  #render a form for editing an existing record.
        pass    