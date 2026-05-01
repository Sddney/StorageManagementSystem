from database.categories_repository import CategoriesRepository
from database.products_repository import ProductsRepository

"""
Database initialization file.
Creates database objects for further use.
"""

DB_PATH = 'database/storage_database.db'  #shared path to the SQLite database file.

#manages the categories and products tables in the database
db_category = CategoriesRepository(DB_PATH)  
db_product = ProductsRepository(DB_PATH)
