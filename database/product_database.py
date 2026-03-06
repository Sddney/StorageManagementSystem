from sqlite3 import *
from abstract_methods import DatabaseMethods


class ProductDatabase(DatabaseMethods):
    def __init__(self, database):
        self.connection = connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products(product_name, product_price, product_quantity, product_id, product_category)")

    def get(self, id):
        self.cursor.execute("SELECT * FROM products WHERE product_id=?", (id))
        return self.cursor.fetchone()
    
    def insert(self, item):
        self.cursor.execute("INSERT INTO products(product_name, product_price, product_quantity, product_id, product_category) VALUES(?, ?, ?, ?)", 
                            (item.get_name(), item.price, item.quantity, item.category, item.get_id()))
        self.connection.commit()
    
    def delete(self, id):
        self.cursor.execute("DELETE FROM products WHERE product_id=?", (id))
        self.connection.commit()

    def update(self, id, item):
        self.cursor.execute("UPDATE products SET product_name=?, product_price=?, product_quantity=? WHERE product_id=?",
                           (item.get_name(), item.price, item.quantity, id))
        self.connection.commit()


