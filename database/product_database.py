from sqlite3 import *
from database.abstract_methods import DatabaseMethods


class ProductDatabase(DatabaseMethods):
    def __init__(self, database):
        self.connection = connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products(product_name TEXT, product_price INTEGER, product_quantity INTEGER, product_category TEXT, product_id INTEGER)""")

    def get_one(self, id):
        self.cursor.execute("SELECT * FROM products WHERE product_id=?", (id,))
        data = self.cursor.fetchone()
        if data is not None:
            return data
        else:
            return None
    
    def insert(self, item):
        self.cursor.execute("INSERT INTO products(product_name, product_price, product_quantity, product_category, product_id) VALUES(?, ?, ?, ?, ?)", 
                            (item.get_name(), item.price, item.quantity, item.category, item.get_id()))
        self.connection.commit()
    
    def delete(self, id):
        self.cursor.execute("DELETE FROM products WHERE product_id=?", (id,))
        self.connection.commit()

    def update(self, id, item):
        self.cursor.execute("UPDATE products SET product_name=?, product_price=?, product_quantity=?, product_category=? WHERE product_id=?",
                           (item.get_name(), item.price, item.quantity, item.category, id))
        self.connection.commit()
    
    def get_all(self):
        self.cursor.execute("SELECT * FROM products")
        data = self.cursor.fetchall()
        if data is not None:
            result = ''
            for row in data:
                result += f"Name: {row[0]}, Price: ${row[1]}, Quantity: {row[2]}, ID: {row[3]}, Category: {row[4]}\n"
            return result
        else:
            return None


