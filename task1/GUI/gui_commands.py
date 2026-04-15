from tkinter import *
from GUI.category_frame import CategoryFrame
from GUI.product_frame import ProductFrame
from GUI.route_frame import RouteFrame

"""
Main GUI entry point.

Combines all GUI modules:
- Products manager
- Categories manager
- Route finder (graph algorithm)

The 800×800 window is divided into three logical areas:
    - Top half    : Products Manager (buttons + dynamic sub-frame)
    - Bottom half : Categories Manager (buttons + dynamic sub-frame)
    - Footer      : 'Route Between Cities' button that overlays the full window
"""

def run_gui():

    # --- Main application window ---
    window = Tk()
    window.title("Storage Management")
    window.geometry('800x800')


    # Products panel
    frame_products = Frame(window, bg = '#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame_products.place(relx=0.05, rely=0.05, relheight=0.4, relwidth=0.9, anchor='nw')

    # Categories panel
    frame_categories = Frame(window, bg='#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
    frame_categories.place(relx=0.05, rely=0.45, relheight=0.4, relwidth=0.9, anchor='nw')

    # Frame managers
    product_frame = ProductFrame(frame_products)
    category_frame = CategoryFrame(frame_categories)
    route_frame = RouteFrame(window)


    lbl_product = Label(frame_products, text="Products\nManager", bg="#E6E6E6", font=("Arial", 16))
    lbl_product.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.2, anchor='nw')

    # --- Products actions buttons ---
    btn_add_product = Button(frame_products, text="Add Product", command=product_frame.add)
    btn_get_storage = Button(frame_products, text="Show Products", command=product_frame.show)
    btn_delete_product = Button(frame_products, text="Delete Product", command=product_frame.delete)
    btn_update_product = Button(frame_products, text="Update Product", command=product_frame.update)

    btn_add_product.place(relx = 0.45, rely=0.1, relwidth=0.2, relheight=0.1, anchor='nw')
    btn_get_storage.place(relx = 0.7, rely= 0.1, relwidth=0.2, relheight=0.1, anchor='nw')
    btn_delete_product.place(relx = 0.45, rely=0.3, relwidth=0.2, relheight=0.1, anchor='nw')
    btn_update_product.place(relx = 0.7, rely=0.3, relwidth=0.2, relheight=0.1, anchor='nw')



    lbl_category = Label(frame_categories, text="Categories\nManager", bg='#E6E6E6', font=("Arial", 16))
    lbl_category.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.2, anchor='nw')


    # --- Categories actions buttons ---
    btn_add_category = Button(frame_categories, text="Add Category", command=category_frame.add)
    btn_show_categories = Button(frame_categories, text="Show Categories", command=category_frame.show)
    btn_delete_category = Button(frame_categories, text="Delete Category", command=category_frame.delete)
    btn_update_category = Button(frame_categories, text="Update Category", command=category_frame.update)

    btn_add_category.place(relx = 0.45, rely=0.1, relwidth=0.2, relheight=0.1, anchor='nw')
    btn_show_categories.place(relx = 0.7, rely=0.1, relwidth=0.2, relheight=0.1, anchor='nw')
    btn_delete_category.place(relx = 0.45, rely=0.3, relwidth=0.2, relheight=0.1, anchor='nw')
    btn_update_category.place(relx = 0.7, rely=0.3, relwidth=0.2, relheight=0.1, anchor='nw')

    # Route finder
    btn_show_route = Button(window, text="Route Between Cities", font=("Arial", 12), command=route_frame.show_route)
    btn_show_route.place(relx=0.05, rely=0.87, relwidth=0.3, relheight=0.07, anchor='nw')

    window.mainloop()



