import GUI.gui_commands
from tkinter import *
#from StorageManager.storage_manager import StorageManager

window = Tk()
window.title("Storage Management")
window.geometry('700x700')

lbl = Label(window, text="Storage")

lbl.grid(column=0, row=0)

#storage_manager = StorageManager()

window.mainloop()