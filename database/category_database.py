from sqlite3 import *
from database.abstract_methods import DatabaseMethods

class CategoryDatabase(DatabaseMethods):
    def __init__(self, database):
        self.connection = connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS categories(category_name TEXT, category_id INTEGER, transport_to TEXT)""")
    
    def get_one(self, id):
        self.cursor.execute("SELECT * FROM categories WHERE category_id=?", (id,))
        return self.cursor.fetchone()
    
    def insert(self, item):
        self.cursor.execute("INSERT INTO categories(category_name, category_id, transport_to) VALUES(?, ?, ?)",
                            (item.get_name(), item.get_id(), item.transport_to))
        self.connection.commit()
    
    def delete(self, id):
        self.cursor.execute("DELETE FROM categories WHERE category_id=?", (id,))
        self.connection.commit()

    def update(self, id, item):
        self.cursor.execute("UPDATE categories SET category_name=?, transport_to=? WHERE category_id=?",
                           (item.get_name(), item.transport_to, id,))
        self.connection.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM categories")
        data = self.cursor.fetchall()
        if data:
            result = ''
            for row in data:
                result += f"Name: {row[0]}, ID: {row[1]}, Transport to: {row[2]}\n"
            return result
        else: 
            return None
    
    def get_categories(self):
        self.cursor.execute("SELECT category_name FROM categories")
        return self.cursor.fetchall()