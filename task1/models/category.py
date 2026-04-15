from models.base_item import BaseItem

class Category(BaseItem):

    """
    Category model, inherits from BaseItem
    Provides getter and setter methods for Product properties
    """

    def __init__(self, name, category_id, transport_to):
        super().__init__(name)
        self.category_id = category_id
        self.transport_to = transport_to

    def get_name(self):
        return self.name

    def get_id(self):
        return self.category_id
    
    def set_name(self, name):
        return super().set_name(name)
    
    def set_transport_to(self, transport_to):
        self.transport_to = transport_to

    def get_description(self):
        print(f"{self.name} - Transport_to: {self.transport_to}")