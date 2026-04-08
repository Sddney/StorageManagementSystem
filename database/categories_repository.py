from sqlite3 import *
from database.repository_base import DatabaseMethods

class CategoriesRepository(DatabaseMethods):   #inheritance from abstract class

    """
    Repository class responsible for managing category data
    Encapsulation of database logic
    """

    def __init__(self, database):   #connects to SQLite database and creates table
        self.connection = connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS categories(category_name TEXT, category_id INTEGER, transport_to TEXT)""")

    def get_one(self, id):  #returns single category based on ID
        self.cursor.execute("SELECT * FROM categories WHERE category_id=?", (id,))
        return self.cursor.fetchone()
    
    def insert(self, item):  #inserts new category into database
        self.cursor.execute("INSERT INTO categories(category_name, category_id, transport_to) VALUES(?, ?, ?)",
                            (item.get_name(), item.get_id(), item.transport_to))
        self.connection.commit()
    
    def delete(self, id):  #deletes category based on ID
        self.cursor.execute("DELETE FROM categories WHERE category_id=?", (id,))
        self.connection.commit()

    def update(self, id, item):   #updates existing category information
        self.cursor.execute("UPDATE categories SET category_name=?, transport_to=? WHERE category_id=?",
                           (item.get_name(), item.transport_to, id,))
        self.connection.commit()

    def get_all(self):  #returns all categories
        self.cursor.execute("SELECT * FROM categories")
        data = self.cursor.fetchall()
        if data is not None:
            return data
        else: 
            return None
    
    def get_categories(self):

        """
        Returns category names.
        Used for dropdown menus in GUI.
        Not part of the abstract interface
        """
        self.cursor.execute("SELECT category_name FROM categories")
        return self.cursor.fetchall()