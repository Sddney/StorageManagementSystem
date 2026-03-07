from models.base_item import BaseItem

class Product(BaseItem):

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

    def get_description(self):
        print(f"{self.name} - ${self.price} - Quantity: {self.quantity}")