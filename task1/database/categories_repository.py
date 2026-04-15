from sqlite3 import *
from database.repository_base import DatabaseMethods

class Node:
    """Node for Binary Search Tree."""
    def __init__(self, key, value):
        self.key = key  # category_id
        self.value = value  # (name, transport_to)
        self.left = None
        self.right = None

class BinarySearchTree:
    """Simple BST for sorted category storage."""
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._insert(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._insert(node.right, key, value)
        # Ignore duplicates

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """Return sorted list of (key, value) tuples."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.key, node.value))
            self._inorder(node.right, result)


class CategoriesRepository(DatabaseMethods):   #inheritance from abstract class

    """
    Repository class responsible for managing category data
    Encapsulation of database logic
    Uses a Binary Search Tree (BST) for sorted in-memory storage and fast lookups.
    """

    def __init__(self, database):   #connects to SQLite database and creates table
        self.connection = connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS categories(category_name TEXT, category_id INTEGER, transport_to TEXT)""")
        self.bst = BinarySearchTree()  
        self.load_bst()

    def load_bst(self):
        """Load all categories from database into BST for sorted access."""
        self.cursor.execute("SELECT * FROM categories")
        rows = self.cursor.fetchall()
        for row in rows:
            self.bst.insert(row[1], (row[0], row[2]))  # id, (name, transport_to)


    def get_one(self, id):  #returns single category based on ID
        node = self.bst.search(id)
        if node:
            return (node.value[0], id, node.value[1])  # (name, id, transport_to)
        # Fallback to DB
        self.cursor.execute("SELECT * FROM categories WHERE category_id=?", (id,))
        data = self.cursor.fetchone()
        if data:
            self.bst.insert(id, (data[0], data[2]))  # Sync BST
            return data
        return None
    
    def insert(self, item):  #inserts new category into database
        self.cursor.execute("INSERT INTO categories(category_name, category_id, transport_to) VALUES(?, ?, ?)",
                            (item.get_name(), item.get_id(), item.transport_to))
        self.connection.commit()
        self.bst.insert(item.get_id(), (item.get_name(), item.transport_to))
    
    def delete(self, id):  #deletes category based on ID
        self.cursor.execute("DELETE FROM categories WHERE category_id=?", (id,))
        self.connection.commit()
        self.bst.delete(id)

    def update(self, id, item):   #updates existing category information
        self.cursor.execute("UPDATE categories SET category_name=?, transport_to=? WHERE category_id=?",
                           (item.get_name(), item.transport_to, id,))
        self.connection.commit()
        self.bst.delete(id)  # Remove old
        self.bst.insert(id, (item.get_name(), item.transport_to))  # Insert updated


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

    def get_sorted_categories(self):
        """Return categories sorted by ID from BST."""
        sorted_list = self.bst.inorder_traversal()
        return [(value[0], key, value[1]) for key, value in sorted_list]  # Format as DB rows
