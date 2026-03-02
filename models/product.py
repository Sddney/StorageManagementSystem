from base_item import BaseItem

class Product(BaseItem):

    def __init__(self, name, price, quantity):
        super().__init__(name)
        self.price = price
        self.quantity = quantity

    def get_description(self):
        return f"{self.name} - ${self.price} - Quantity: {self.quantity}"