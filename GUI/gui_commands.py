from tkinter import *
from tkinter import messagebox
from random import randint
from database.product_database import ProductDatabase
from database.category_database import CategoryDatabase
from models.product import Product
from models.category import Category

db_product = ProductDatabase('products_storage.db')
db_category = CategoryDatabase('categories_storage.db')

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
    category = Entry(frame, width=20)

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
    categoty = Entry(frame, width=20)

    name.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.15, anchor='nw')
    price.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.15, anchor='nw')
    quantity.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.15, anchor='nw')
    categoty.place(relx=0.5, rely=0.9, relwidth=0.3, relheight=0.15, anchor='nw')

    def commit():
        if db_product.get_one(id.get()) == None:
            messagebox.showerror("Storage", "This product does not exist!")
            frame.destroy()
            return
        new_product = Product(name.get(), price.get(), quantity.get(), categoty.get(), id.get())
        db_product.update(id.get(), new_product)
        messagebox.showinfo("Storage", "Product updated successfully!")
        frame.destroy()

    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.2, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')



def add_category():
    frame = Frame(window, bg='white')
    frame.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor='nw')
    
    Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    Label(frame, text="Transport to:").grid(row=1, column=0, padx=10, pady=10, sticky="e")

    name = Entry(frame, width=20)
    transport_to = Entry(frame, width=20)
   
    name.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')
    transport_to.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.15, anchor='nw')

    def commit():
        for i in range(10000):
            id = randint(1000, 9999)
            if db_category.get_one(id) == None:
                new_category = Category(name.get(), id, transport_to.get())
                db_category.insert(new_category)
                messagebox.showinfo("Storage", "Category added successfully!")
                frame.destroy()
                break
    
    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.5, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')


def show_categories():
    messagebox.showinfo("Storage", db_category.get_all())


def delete_category():
    frame = Frame(window, bg='white')
    frame.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor='nw')

    Label(frame, text="Enter a category's ID").grid(row=1, column=0, padx=10, pady=10, sticky="e")

    id = Entry(frame, width=20)
    id.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')


    def delete():
        if db_category.get_one(id.get()) == None:
            messagebox.showerror("Storage", "This category does not exist!")
            frame.destroy()
            return
        db_category.delete(id.get())
        messagebox.showinfo("Storage", "Category deleted successfully!")
        frame.destroy()

    btn_delete = Button(frame, text="Delete", command=delete)
    btn_delete.place(relx=0.5, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')


def update_category():
    frame = Frame(window, bg='white')
    frame.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor='nw')

    Label(frame, text="ID:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    Label(frame, text="Name:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    Label(frame, text="Transport to:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    
    
    id = Entry(frame, width=20)
    id.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')
    
    name = Entry(frame, width=20)
    transport_to = Entry(frame, width=20)

    name.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.15, anchor='nw')
    transport_to.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.15, anchor='nw')

    def commit():
        if db_category.get_one(id.get()) == None:
            messagebox.showerror("Storage", "This product does not exist!")
            frame.destroy()
            return
        new_category = Category(name.get(), id.get(), transport_to.get())
        db_category.update(id.get(), new_category)
        messagebox.showinfo("Storage", "Product updated successfully!")
        frame.destroy()

    btn_commit = Button(frame, text="Commit", command=commit)
    btn_commit.place(relx=0.5, rely=0.9, relwidth=0.2, relheight=0.1, anchor='nw')




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

window.mainloop()