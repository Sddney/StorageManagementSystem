from base_item import BaseItem

class Category(BaseItem):

    def __init__(self, name, category_id, transport_to):
        super().__init__(name)
        self.category_id = category_id
        self.transport_to = transport_to

    def get_name(self):
        return self.name

    def get_id(self):
        return self.category_id

    def get_description(self):
        print(f"{self.name} - Transport_to: {self.transport_to}")