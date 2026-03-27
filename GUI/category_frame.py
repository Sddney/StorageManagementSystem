from tkinter import *
from tkinter import messagebox, ttk
from random import randint
from database.product_database import ProductDatabase
from database.category_database import CategoryDatabase
from models.product import Product
from models.category import Category
from algorithm.dijkstra_algorithm import ReturnCities
from GUI.abstract_frame import AbstractFrame

db_category = CategoryDatabase('categories_storage.db')

class CategoryFrame(AbstractFrame):
    
    def __init__(self, parent):
        super().__init__(parent)

    def Add(self):
        frame = Frame(self.parent, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
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


    def Show(self):
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
            table.column(he, anchor='center', width=500//3, stretch=False)

        for row in lst:
            table.insert("", END, values=row)

        table.pack(fill=BOTH, expand=True)

        storage_window.mainloop()
        #messagebox.showinfo("Storage", db_category.get_all())


    def Delete(self):
        frame = Frame(self.parent, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
        frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')

        Label(frame, text="Enter a category's ID:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')

        id = Entry(frame, width=20)
        id.place(relx=0.35, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')


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


    def Update(self):
        frame = Frame(self.parent, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
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
