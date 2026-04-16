from tkinter import *
from tkinter import messagebox, ttk
from random import randint
from models.product import Product
from GUI.abstract_frame import AbstractFrame
from database.databases_initialization import db_category, db_product

class ProductFrame(AbstractFrame):

    """
    GUI class handles user interaction related to product management
    Implements abstract methods from AbstractFrame
    """

    def __init__(self, parent):
        super().__init__(parent)

    def add(self):

        """
        Renders a form that lets the user create a new product with a unique ID
        """
        frame = Frame(self.parent, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
        frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')

        Label(frame, text="Name:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Price(HKD):", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Quantity:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Category:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        
        # --- Input fields ---
        name = Entry(frame, width=20)
        price = Entry(frame, width=20)
        quantity = Entry(frame, width=20)
        category = ttk.Combobox(frame, values=db_category.get_categories(), state='readonly')  #create category dropdown dynamically from the database

        name.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
        price.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        quantity.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
        category.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')

        #inner commit function
        def commit():
            """
            Generates a unique ID and insert a new product into the database if doesn't exist
            Closes the form
            """
            for i in range(10000):
                product_id = randint(1000, 9999)
                if db_product.get_one(product_id) == None:
                    new_product = Product(name.get(), price.get(), quantity.get(), category.get(), product_id)
                    db_product.insert(new_product)
                    messagebox.showinfo("Storage", "Product added successfully!")
                    frame.destroy()
                    break
        
        def back(): #close the form without saving
            frame.destroy()
        
        # --- Action buttons ---
        btn_back = Button(frame, text="Back", command=back)
        btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
        
        btn_commit = Button(frame, text="Commit", command=commit)
        btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
        

    def show(self):
        """
        Renders a table with all products in the database
        """
        storage_window = Tk()
        storage_window.title("Storage")
        storage_window.geometry('500x500')

        lst = db_product.get_all()  #fetch all products records from the database
        heads = ["Name", "Price(HKD)", "Quantity", "Category", "ID"]
        table = ttk.Treeview(storage_window, show='headings', columns=heads)

        style = ttk.Style(table)
        style.theme_use('default')
        style.configure('Treeview', bordercolor="#E8E8E8", borderwidth=1)

        #configure each column header and width
        for he in heads:
            table.heading(he, text=he, anchor='center')
            table.column(he, anchor='center', width=100, stretch=False)

        for row in lst:
            table.insert("", END, values=row)

        table.pack(fill=BOTH, expand=True)

        storage_window.mainloop()




    def delete(self):

        """
        Renders a form that lets the user delete a product by id
        """
        frame = Frame(self.parent, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
        frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')

        Label(frame, text="Enter a product's ID", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')

        product_id = Entry(frame, width=20)
        product_id.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')


        def delete():
            """
            Validate existence and delete a product by id from the database
            """
            if db_product.get_one(product_id.get()) == None:
                messagebox.showerror("Storage", "This product does not exist!")
                frame.destroy()
                return
            db_product.delete(product_id.get())
            messagebox.showinfo("Storage", "Product deleted successfully!")
            frame.destroy()

        def back(): #close the form 
            frame.destroy()
        
        # --- Action buttons ---
        btn_back = Button(frame, text="Back", command=back)
        btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
        
        btn_delete = Button(frame, text="Delete", command=delete)
        btn_delete.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')



    def update(self):
        """
        Renders a form that lets the user update a product by id
        """
        
        frame = Frame(self.parent, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
        frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')
        
        id = Entry(frame, width=20)
        id.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')


        Label(frame, text="ID:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Name:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Price(HKD):", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Quantity:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Category:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')

        # --- Input fields ---
        name = Entry(frame, width=20)
        price = Entry(frame, width=20)
        quantity = Entry(frame, width=20)
        category = ttk.Combobox(frame, values=db_category.get_categories(), state='readonly')

        name.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        price.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')
        quantity.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        category.place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')

        def commit():
            """
            Validate existence and update a product by id in the database
            """
            if db_product.get_one(id.get()) == None:
                messagebox.showerror("Storage", "This product does not exist!")
                frame.destroy()
                return
            new_product = Product(name.get(), price.get(), quantity.get(), category.get(), id.get())
            db_product.update(id.get(), new_product)
            messagebox.showinfo("Storage", "Product updated successfully!")
            frame.destroy()

        def back():   #close the form
            frame.destroy()
        
        # --- Action buttons ---
        btn_back = Button(frame, text="Back", command=back)
        btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
        
        btn_commit = Button(frame, text="Commit", command=commit)
        btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
