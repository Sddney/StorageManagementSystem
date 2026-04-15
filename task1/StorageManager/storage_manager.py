from sqlite3 import *


def create_database():
    connection = connect("storage.db")

    cursor = connection.cursor()

    command1 = """CREATE TABLE IF NOT EXISTS
                products(
                    product_id INTEGER PRIMARY KEY,
                    product_name TEXT,
                    product_price INTEGER,
                    product_quantity INTEGER
                    product_to_transport
                    product_category TEXT)"""
    
    cursor.execute(command1)
    connection.commit()
    connection.close()



