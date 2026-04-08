from models.base_item import BaseItem

class Product(BaseItem):

    """
    Product model, inherits from BaseItem
    Provides getter and setter methods for Product properties
    """

    def __init__(self, name, price, quantity, category, id):
        super().__init__(name)
        self.price = price
        self.quantity = quantity
        self.category = category
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id
    
    def set_name(self, name):
        return super().set_name(name)
    
    def set_price(self, price):
        self.price = price
    
    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_category(self, category):
        self.category = category 

    def get_description(self):
        print(f"{self.name} - ${self.price} - Quantity: {self.quantity}")