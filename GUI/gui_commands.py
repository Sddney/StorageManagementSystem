from tkinter import *
from tkinter import messagebox, ttk
from random import randint
from database.products_repository import ProductRepository
from database.categories_repository import CategoryRepository
from models.product import Product
from models.category import Category
from algorithm.dijkstra_algorithm import Dijkstra, ReturnCities
import json


db_product = ProductRepository('products_storage.db')
db_category = CategoryRepository('categories_storage.db')

def add_product():
    frame = Frame(window, bg='lightgreen')
    frame.place(relx=0.5, rely=0, relheight=0.5, relwidth=0.5, anchor='nw')

    Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    Label(frame, text="Price:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    Label(frame, text="Quantity:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    Label(frame, text="Category:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    
    name = Entry(frame, width=20)
    price = Entry(frame, width=20)
    quantity = Entry(frame, width=20)
    category = ttk.Combobox(frame, values=db_category.get_categories(), state='readonly')

    name.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')
    price.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.15, anchor='nw')
    quantity.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.15, anchor='nw')
    category.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.15, anchor='nw')


    def commit():
        for i in range(10000):
            product_id = randint(1000, 9999)
            if db_product.get_one(product_id) == None:
                new_product = Product(name.get(), price.get(), quantity.get(), category.get(), product_id)
                db_product.insert(new_product)
                messagebox.showinfo("Storage", "Product added successfully!")
                frame.destroy()
                break
    
    def back():
        frame.destroy()
    
    btn_back = Button(frame, text="Back", command=back)
    btn_back.place(relx=0.3, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')
    
    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.5, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')
    

def show_products():
    messagebox.showinfo("Storage", db_product.get_all())



def delete_product():
    frame = Frame(window, bg='lightgreen')
    frame.place(relx=0.5, rely=0, relheight=0.5, relwidth=0.5, anchor='nw')

    Label(frame, text="Enter a product's ID").grid(row=1, column=0, padx=10, pady=10, sticky="e")

    product_id = Entry(frame, width=20)
    product_id.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')


    def delete():
        if db_product.get_one(product_id.get()) == None:
            messagebox.showerror("Storage", "This product does not exist!")
            frame.destroy()
            return
        db_product.delete(product_id.get())
        messagebox.showinfo("Storage", "Product deleted successfully!")
        frame.destroy()

    def back():
        frame.destroy()
    
    btn_back = Button(frame, text="Back", command=back)
    btn_back.place(relx=0.3, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')

    btn_delete = Button(frame, text="Delete", command=delete)
    btn_delete.place(relx=0.5, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')



def update_product():
    frame = Frame(window, bg='lightgreen')
    frame.place(relx=0.5, rely=0, relheight=0.5, relwidth=0.5, anchor='nw')
    
    id = Entry(frame, width=20)
    id.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')


    Label(frame, text="ID:").grid(row=1, column=0, padx=0, pady=10, sticky="e")
    Label(frame, text="Name:").grid(row=2, column=0, padx=0, pady=10, sticky="e")
    Label(frame, text="Price:").grid(row=3, column=0, padx=0, pady=10, sticky="e")
    Label(frame, text="Quantity:").grid(row=4, column=0, padx=0, pady=10, sticky="e")
    Label(frame, text="Category:").grid(row=5, column=0, padx=0, pady=10, sticky="e")

    name = Entry(frame, width=20)
    price = Entry(frame, width=20)
    quantity = Entry(frame, width=20)
    category = ttk.Combobox(frame, values=db_category.get_categories(), state='readonly')

    name.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')
    price.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.15, anchor='nw')
    quantity.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.15, anchor='nw')
    category.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.15, anchor='nw')

    def commit():
        if db_product.get_one(id.get()) == None:
            messagebox.showerror("Storage", "This product does not exist!")
            frame.destroy()
            return
        new_product = Product(name.get(), price.get(), quantity.get(), category.get(), id.get())
        db_product.update(id.get(), new_product)
        messagebox.showinfo("Storage", "Product updated successfully!")
        frame.destroy()

    def back():
        frame.destroy()
    
    btn_back = Button(frame, text="Back", command=back)
    btn_back.place(relx=0.2, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')

    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.7, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')



def add_category():
    frame = Frame(window, bg='lightgreen')
    frame.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor='nw')
    
    Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    Label(frame, text="Transport to:").grid(row=1, column=0, padx=10, pady=10, sticky="e")

    name = Entry(frame, width=20)
    transport_to = ttk.Combobox(frame, values=ReturnCities(), state='readonly')
   
    name.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')
    transport_to.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.15, anchor='nw')

    def commit():
        for i in range(10000):
            id = randint(1000, 9999)
            if db_category.get_by_id(id) == None:
                new_category = Category(name.get(), id, transport_to.get())
                db_category.insert(new_category)
                messagebox.showinfo("Storage", "Category added successfully!")
                frame.destroy()
                break

    def back():
        frame.destroy()
    
    btn_back = btn_back = Button(frame, text="Back", command=back)
    btn_back.place(relx=0.3, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')
    
    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.5, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')


def show_categories():
    messagebox.showinfo("Storage", db_category.get_all())


def delete_category():
    frame = Frame(window, bg='lightgreen')
    frame.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor='nw')

    Label(frame, text="Enter a category's ID").grid(row=1, column=0, padx=10, pady=10, sticky="e")

    id = Entry(frame, width=20)
    id.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')


    def delete():
        if db_category.get_by_id(id.get()) == None:
            messagebox.showerror("Storage", "This category does not exist!")
            frame.destroy()
            return
        db_category.delete(id.get())
        messagebox.showinfo("Storage", "Category deleted successfully!")
        frame.destroy()
    
    def back():
        frame.destroy()
    
    btn_back = btn_back = Button(frame, text="Back", command=back)
    btn_back.place(relx=0.3, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')

    btn_delete = Button(frame, text="Delete", command=delete)
    btn_delete.place(relx=0.5, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')


def update_category():
    frame = Frame(window, bg='lightgreen')
    frame.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor='nw')

    Label(frame, text="ID:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    Label(frame, text="Name:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    Label(frame, text="Transport to:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    
    
    id = Entry(frame, width=20)
    id.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')
    
    name = Entry(frame, width=20)
    transport_to = ttk.Combobox(frame, values=ReturnCities(), state='readonly')

    name.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.15, anchor='nw')
    transport_to.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.15, anchor='nw')

    def commit():
        if db_category.get_by_id(id.get()) == None:
            messagebox.showerror("Storage", "This product does not exist!")
            frame.destroy()
            return
        new_category = Category(name.get(), id.get(), transport_to.get())
        db_category.update(id.get(), new_category)
        messagebox.showinfo("Storage", "Product updated successfully!")
        frame.destroy()

    def back():
        frame.destroy()
    
    btn_back = btn_back = Button(frame, text="Back", command=back)
    btn_back.place(relx=0.5, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')

    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.7, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')


def show_route():
    with open("algorithm/cities.json") as f:
        graph = json.load(f)
    
    frame_cities = Frame(window, bg='lightyellow')
    frame_cities.place(relx=0, rely=0, relheight=1, relwidth=1, anchor='nw')

    city_from = ttk.Combobox(frame_cities, values=ReturnCities(), state='readonly')
    city_from.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.05, anchor='nw')
    city_from.current(0)

    city_to = ttk.Combobox(frame_cities, values=ReturnCities(), state='readonly')
    city_to.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.05, anchor='nw')
    city_to.current(0)

    def show():
        if city_from.get() == city_to.get():
            messagebox.showerror("Route", "Choose different cities!")
            return
        result = Dijkstra(graph, city_from.get(), city_to.get())
        if result == 'Path not reachable':
            messagebox.showerror("Route", "Path not reachable")
            return
        
        distance, path = result
        messagebox.showinfo("Route", "Distance between cities: " + str(distance) + "\nPath: " + ' -> '.join(path))

    btn_show = Button(frame_cities, text="Show Route", command=show)
    btn_show.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1, anchor='nw')

    def Back():
        frame_cities.destroy()

    btn_back = Button(frame_cities, text="Back", command=Back)
    btn_back.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.05, anchor='nw')

        


window = Tk()
window.title("Storage Management")
window.geometry('700x700')


frame_products = Frame(window, bg = 'lightgrey')
frame_products.place(relx=0, rely=0, relheight=0.5, relwidth=1, anchor='nw')

lbl_product = Label(frame_products, text="Products Manager", bg='lightgrey')
lbl_product.pack()

btn_add_product = Button(frame_products, text="Add Product", command=add_product)
btn_get_storage = Button(frame_products, text="See Storage", command=show_products)
btn_delete_product = Button(frame_products, text="Delete Product", command=delete_product)
btn_update_product = Button(frame_products, text="Update Product", command=update_product)

btn_add_product.place(relx = 0.1, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')
btn_get_storage.place(relx = 0.1, rely= 0.3, relwidth=0.3, relheight=0.15, anchor='nw')
btn_delete_product.place(relx = 0.1, rely=0.5, relwidth=0.3, relheight=0.15, anchor='nw')
btn_update_product.place(relx = 0.1, rely=0.7, relwidth=0.3, relheight=0.15, anchor='nw')

#############################################################################################

frame_categories = Frame(window, bg='lightblue')
frame_categories.place(relx=0, rely=0.5, relheight=0.5, relwidth=1, anchor='nw')

lbl_category = Label(frame_categories, text="Categories Manager", bg='lightblue')
lbl_category.pack()

btn_add_category = Button(frame_categories, text="Add Category", command=add_category)
btn_show_categories = Button(frame_categories, text="Show Categories", command=show_categories)
btn_delete_category = Button(frame_categories, text="Delete Category", command=delete_category) 
btn_update_category = Button(frame_categories, text="Update Category", command=update_category)

btn_add_category.place(relx = 0.1, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')
btn_show_categories.place(relx = 0.1, rely=0.3, relwidth=0.3, relheight=0.15, anchor='nw')
btn_delete_category.place(relx = 0.1, rely=0.5, relwidth=0.3, relheight=0.15, anchor='nw')
btn_update_category.place(relx = 0.1, rely=0.7, relwidth=0.3, relheight=0.15, anchor='nw')

btn_show_route = Button(window, text="Show Route Between Cities", command=show_route)
btn_show_route.place(relx=0.1, rely=0.46, relwidth=0.3, relheight=0.08, anchor='nw')

window.mainloop()