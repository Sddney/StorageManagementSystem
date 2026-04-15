from tkinter import *
from tkinter import messagebox, ttk
from random import randint
from task1.models.category import Category
from task1.algorithm.dijkstra_algorithm import return_cities
from task1.GUI.abstract_frame import AbstractFrame
from task1.database.databases_initialization import db_category

class CategoryFrame(AbstractFrame):

    """
    GUI class handles user interaction related to category management
    Implements abstract methods from AbstractFrame
    
    """
    
    def __init__(self, parent):
        super().__init__(parent)

    def add(self):    
        
        """
        Renders a form that lets the user create a new category with a unique ID
        """
        
        frame = Frame(self.parent, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
        frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')
        
        Label(frame, text="Name:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Transport to:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        
        # --- Input fields ---
        name = Entry(frame, width=20)
        transport_to = ttk.Combobox(frame, values=return_cities(), state='readonly') #create the destination dropdown from the cities graph
    
        name.place(relx=0.3, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
        transport_to.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')

        #inner commit function
        def commit():
            """
            Generates a unique 4-digit id and inserts a Category object in the database if it doesn't exist
            Closes the form.
            """
            for i in range(10000):
                id = randint(1000, 9999)
                if db_category.get_one(id) == None:
                    new_category = Category(name.get(), id, transport_to.get())
                    db_category.insert(new_category)
                    messagebox.showinfo("Storage", "Category added successfully!")
                    frame.destroy()
                    break

        def back():  #close the form without saving
            frame.destroy()
        

        # --- Action buttons ---
        btn_back = Button(frame, text="Back", command=back)
        btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
        
        btn_commit = Button(frame, text="Commit", command=commit)
        btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')


    def show(self):  
        
        """
        Renders a table with all categories in the database
        """
        
        storage_window = Tk()
        storage_window.title("Storage")
        storage_window.geometry('500x500')

        lst = db_category.get_all() #fetch all categories records from the database
        heads = ["Name", "ID", "Transport to"]
        table = ttk.Treeview(storage_window, show='headings', columns=heads)

        style = ttk.Style(table)
        style.theme_use('default')
        style.configure('Treeview', bordercolor="#E8E8E8", borderwidth=1)

        #configure each column header and width
        for he in heads:  
            table.heading(he, text=he, anchor='center')
            table.column(he, anchor='center', width=500//3, stretch=False)

        for row in lst:
            table.insert("", END, values=row)

        table.pack(fill=BOTH, expand=True)

        storage_window.mainloop()


    def delete(self):

        """
        Display a form to delete a category by its id
        """
        
        frame = Frame(self.parent, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
        frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')

        Label(frame, text="Enter a category's ID:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.15, anchor='nw')

        id = Entry(frame, width=20)  #id input field
        id.place(relx=0.35, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')


        def delete():

            """
            Validate existence and delete a category by id from the database
            """
            if db_category.get_one(id.get()) == None:
                messagebox.showerror("Storage", "This category does not exist!")
                frame.destroy()
                return
            db_category.delete(id.get())
            messagebox.showinfo("Storage", "Category deleted successfully!")
            frame.destroy()
        
        def back():   #close the form 
            frame.destroy()
        

        # --- Action buttons ---
        btn_back = Button(frame, text="Back", command=back)
        btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
        
        btn_commit = Button(frame, text="Delete", command=delete)
        btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')


    def update(self):

        """
        Display a form to update a category by its id
        """
        frame = Frame(self.parent, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
        frame.place(relx=0.1, rely=0.45, relheight=0.5, relwidth=0.8, anchor='nw')

        Label(frame, text="ID:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Name:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        Label(frame, text="Transport to:", bg = '#E6E6E6', font=("Arial", 10)).place(relx=0, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')
        
        # --- Input fields ---
        id = Entry(frame, width=20)
        id.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.15, anchor='nw')
        
        name = Entry(frame, width=20)
        transport_to = ttk.Combobox(frame, values=return_cities(), state='readonly')

        name.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15, anchor='nw')
        transport_to.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.15, anchor='nw')

        def commit():
            """
            Validate existence and update a category by id in the database
            """
            if db_category.get_one(id.get()) == None:
                messagebox.showerror("Storage", "This product does not exist!")
                frame.destroy()
                return
            new_category = Category(name.get(), id.get(), transport_to.get())
            db_category.update(id.get(), new_category)
            messagebox.showinfo("Storage", "Product updated successfully!")
            frame.destroy()

        def back():  #close the form
            frame.destroy()
        
        # --- Action buttons ---
        btn_back = Button(frame, text="Back", command=back)
        btn_back.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
        
        btn_commit = Button(frame, text="Commit", command=commit)
        btn_commit.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='nw')
