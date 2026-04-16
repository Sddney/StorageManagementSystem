from sqlite3 import *
from database.repository_base import DatabaseMethods


class ProductsRepository(DatabaseMethods):

    """
    Repository class responsible for managing products data.
    Encapsulation of database logic
    
    """

    def __init__(self, database):   #connects to SQLite database and creates table
        self.connection = connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products(product_name TEXT, product_price INTEGER, product_quantity INTEGER, product_category TEXT, product_id INTEGER)""")

    def get_one(self, id):   #returns single product based on id
        self.cursor.execute("SELECT * FROM products WHERE product_id=?", (id,))
        data = self.cursor.fetchone()
        if data is not None:
            return data
        else:
            return None
    
    def insert(self, item):   #inserts new product into database
        self.cursor.execute("INSERT INTO products(product_name, product_price, product_quantity, product_category, product_id) VALUES(?, ?, ?, ?, ?)",
                            (item.get_name(), item.price, item.quantity, item.category, item.get_id()))
        self.connection.commit()
    
    def delete(self, id): #deletes product based on id
        self.cursor.execute("DELETE FROM products WHERE product_id=?", (id,))
        self.connection.commit()

    def update(self, id, item):  #updates existing product information
        self.cursor.execute("UPDATE products SET product_name=?, product_price=?, product_quantity=?, product_category=? WHERE product_id=?",
                           (item.get_name(), item.price, item.quantity, item.category, id))
        self.connection.commit()
    
    def get_all(self): #returns all products
        self.cursor.execute("SELECT * FROM products")
        data = self.cursor.fetchall()
        if data is not None:
            return data
        else:
            return None

