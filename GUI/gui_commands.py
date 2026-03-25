from tkinter import *
from tkinter import messagebox, ttk
from random import randint
from database.product_database import ProductDatabase
from database.category_database import CategoryDatabase
from models.product import Product
from models.category import Category
from algorithm.dijkstra_algorithm import Dijkstra, ReturnCities
import json

with open("algorithm/cities.json") as f:
        graph = json.load(f)


db_product = ProductDatabase('products_storage.db')
db_category = CategoryDatabase('categories_storage.db')

label_distance, label_path = None, None

def add_product():
    frame = Frame(frame_products, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')

    Label(frame, text="Name:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Price:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Quantity:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Category:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    
    name = Entry(frame, width=20)
    price = Entry(frame, width=20)
    quantity = Entry(frame, width=20)
    category = ttk.Combobox(frame, values=db_category.get_categories(), state='readonly')

    name.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
    price.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    quantity.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
    category.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')


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
    btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
    
    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
    

def show_products():
    storage_window = Tk()
    storage_window.title("Storage")
    storage_window.geometry('500x500')

    lst = db_product.get_all()
    heads = ["Name", "Price", "Quantity", "ID", "Category"]
    table = ttk.Treeview(storage_window, show='headings', columns=heads)

    style = ttk.Style(table)
    style.theme_use('default')
    style.configure('Treeview', bordercolor="#E8E8E8", borderwidth=1)

    for he in heads:
        table.heading(he, text=he, anchor='center')
        table.column(he, anchor='center', width=100, stretch=False)

    for row in lst:
        table.insert("", END, values=row)

    table.pack(fill=BOTH, expand=True)

    storage_window.mainloop()


    #messagebox.showinfo("Storage", db_product.get_all())



def delete_product():
    frame = Frame(frame_products, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')

    Label(frame, text="Enter a product's ID", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')

    product_id = Entry(frame, width=20)
    product_id.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')


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
    btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')

    btn_delete = Button(frame, text="Delete", command=delete)
    btn_delete.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')



def update_product():
    
    frame = Frame(frame_products, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')
    
    id = Entry(frame, width=20)
    id.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')


    Label(frame, text="ID:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Name:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Price:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Quantity:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Category:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')

    name = Entry(frame, width=20)
    price = Entry(frame, width=20)
    quantity = Entry(frame, width=20)
    category = ttk.Combobox(frame, values=db_category.get_categories(), state='readonly')

    name.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    price.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')
    quantity.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    category.place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')

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
    btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
    
    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')



def add_category():
    frame = Frame(frame_categories, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')
    
    Label(frame, text="Name:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Transport to:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    
    name = Entry(frame, width=20)
    transport_to = ttk.Combobox(frame, values=ReturnCities(), state='readonly')
   
    name.place(relx=0.3, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
    transport_to.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')

    def commit():
        for i in range(10000):
            id = randint(1000, 9999)
            if db_category.get_one(id) == None:
                new_category = Category(name.get(), id, transport_to.get())
                db_category.insert(new_category)
                messagebox.showinfo("Storage", "Category added successfully!")
                frame.destroy()
                break

    def back():
        frame.destroy()
    
    btn_back = Button(frame, text="Back", command=back)
    btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
    
    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')


def show_categories():
    storage_window = Tk()
    storage_window.title("Storage")
    storage_window.geometry('500x500')

    lst = db_category.get_all()
    heads = ["Name", "ID", "Transport to"]
    table = ttk.Treeview(storage_window, show='headings', columns=heads)

    style = ttk.Style(table)
    style.theme_use('default')
    style.configure('Treeview', bordercolor="#E8E8E8", borderwidth=1)

    for he in heads:
        table.heading(he, text=he, anchor='center')
        table.column(he, anchor='center', width=100, stretch=False)

    for row in lst:
        table.insert("", END, values=row)

    table.pack(fill=BOTH, expand=True)

    storage_window.mainloop()
    #messagebox.showinfo("Storage", db_category.get_all())


def delete_category():
    frame = Frame(frame_categories, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')

    Label(frame, text="Enter a category's ID:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')

    id = Entry(frame, width=20)
    id.place(relx=0.3, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')


    def delete():
        if db_category.get_one(id.get()) == None:
            messagebox.showerror("Storage", "This category does not exist!")
            frame.destroy()
            return
        db_category.delete(id.get())
        messagebox.showinfo("Storage", "Category deleted successfully!")
        frame.destroy()
    
    def back():
        frame.destroy()
    
    btn_back = Button(frame, text="Back", command=back)
    btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
    
    btn_commit = Button(frame, text="Delete", command=delete)
    btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')


def update_category():
    frame = Frame(frame_categories, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')

    Label(frame, text="ID:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Name:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    Label(frame, text="Transport to:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')
    
    
    id = Entry(frame, width=20)
    id.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
    
    name = Entry(frame, width=20)
    transport_to = ttk.Combobox(frame, values=ReturnCities(), state='readonly')

    name.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
    transport_to.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')

    def commit():
        if db_category.get_one(id.get()) == None:
            messagebox.showerror("Storage", "This product does not exist!")
            frame.destroy()
            return
        new_category = Category(name.get(), id.get(), transport_to.get())
        db_category.update(id.get(), new_category)
        messagebox.showinfo("Storage", "Product updated successfully!")
        frame.destroy()

    def back():
        frame.destroy()
    
    btn_back = Button(frame, text="Back", command=back)
    btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
    
    btn_commit = Button(frame, text="Delete", command=commit)
    btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')


def show_route():
    
    frame = Frame(window, bg='#E6E6E6')
    frame.place(relx=0, rely=0, relheight=1, relwidth=1, anchor='nw')

    frame_cities = Frame(frame, bg='#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame_cities.place(relx=0.05, rely=0.05, relheight=0.55, relwidth=0.9, anchor='nw')

    frame_route = Frame(frame, bg='#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame_route.place(relx=0.05, rely=0.65, relheight=0.3, relwidth=0.9, anchor='nw')

    
    Label(frame_cities, text='Finding the closest route and distance between\ncities for transportation',  bg = '#E6E6E6', font=("Arial", 13)).place(relx=0.3, rely=0.1)

    Label(frame_cities, text='From: ', bg = '#E6E6E6', font=("Arial", 12)).place(relx=0.1, rely=0.3)
    Label(frame_cities, text='Towards: ', bg = '#E6E6E6', font=("Arial", 12)).place(relx=0.1, rely=0.6)

    city_from = ttk.Combobox(frame_cities, values=ReturnCities(), state='readonly')
    city_from.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1, anchor='nw')
    city_from.current(0)

    city_to = ttk.Combobox(frame_cities, values=ReturnCities(), state='readonly')
    city_to.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1, anchor='nw')
    city_to.current(0)

    def show():

        global label_distance, label_path

        if label_distance:
            label_distance.destroy()
        if label_path:
            label_path.destroy()

        if city_from.get() == city_to.get():
            messagebox.showerror("Route", "Choose different cities!")
            return
        result = Dijkstra(graph, city_from.get(), city_to.get())
        if result == 'Path not reachable':
            messagebox.showerror("Route", "Path not reachable")
            return
        
        distance, path = result
        distance_text = "Distance between cities: " + str(distance) 
        path_text = "\nPath: " + ' ---> '.join(path)

        label_distance = Label(frame_route, text=distance_text, bg = '#E6E6E6', font=("Arial", 12))
        label_distance.place(relx=0.1, rely=0.3)
        label_path = Label(frame_route, text=path_text, bg = '#E6E6E6', font=("Arial", 12), wraplength=600)
        label_path.place(relx=0.1, rely=0.5)

        #messagebox.showinfo("Route", "Distance between cities: " + str(distance) + "\nPath: " + ' -> '.join(path))

    btn_show = Button(frame_cities, text="Show Route", command=show)
    btn_show.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.1, anchor='nw')

    def Back():
        global label_distance, label_path
        label_distance, label_path = None, None
        frame.destroy()

    btn_back = Button(frame, text="Back", command=Back)
    btn_back.place(relx=0.6, rely=0.7, relwidth=0.2, relheight=0.1, anchor='nw')

        


window = Tk()
window.title("Storage Management")
window.geometry('800x800')


frame_products = Frame(window, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
frame_products.place(relx=0.05, rely=0.05, relheight=0.4, relwidth=0.9, anchor='nw')

lbl_product = Label(frame_products, text="Products\nManager", bg="#E6E6E6", font=("Arial", 16))
lbl_product.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.2, anchor='nw')

btn_add_product = Button(frame_products, text="Add Product", command=add_product)
btn_get_storage = Button(frame_products, text="Show Products", command=show_products)
btn_delete_product = Button(frame_products, text="Delete Product", command=delete_product)
btn_update_product = Button(frame_products, text="Update Product", command=update_product)

btn_add_product.place(relx = 0.45, rely=0.1, relwidth=0.2, relheight=0.1, anchor='nw')
btn_get_storage.place(relx = 0.7, rely= 0.1, relwidth=0.2, relheight=0.1, anchor='nw')
btn_delete_product.place(relx = 0.45, rely=0.3, relwidth=0.2, relheight=0.1, anchor='nw')
btn_update_product.place(relx = 0.7, rely=0.3, relwidth=0.2, relheight=0.1, anchor='nw')

#############################################################################################

frame_categories = Frame(window, bg='#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
frame_categories.place(relx=0.05, rely=0.45, relheight=0.4, relwidth=0.9, anchor='nw')

lbl_category = Label(frame_categories, text="Categories\nManager", bg='#E6E6E6', font=("Arial", 16))
lbl_category.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.2, anchor='nw')

btn_add_category = Button(frame_categories, text="Add Category", command=add_category)
btn_show_categories = Button(frame_categories, text="Show Categories", command=show_categories)
btn_delete_category = Button(frame_categories, text="Delete Category", command=delete_category) 
btn_update_category = Button(frame_categories, text="Update Category", command=update_category)

btn_add_category.place(relx = 0.45, rely=0.1, relwidth=0.2, relheight=0.1, anchor='nw')
btn_show_categories.place(relx = 0.7, rely=0.1, relwidth=0.2, relheight=0.1, anchor='nw')
btn_delete_category.place(relx = 0.45, rely=0.3, relwidth=0.2, relheight=0.1, anchor='nw')
btn_update_category.place(relx = 0.7, rely=0.3, relwidth=0.2, relheight=0.1, anchor='nw')

btn_show_route = Button(window, text="Route Between Cities", font=("Arial", 12), command=show_route)
btn_show_route.place(relx=0.05, rely=0.87, relwidth=0.3, relheight=0.07, anchor='nw')

window.mainloop()