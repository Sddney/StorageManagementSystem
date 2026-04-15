from tkinter import *
from tkinter import messagebox, ttk

from task2.dijkstra.dijkstra_algorithm import dijkstra, return_cities
import json

with open("task2/dijkstra/cities.json") as f:
        graph = json.load(f)


# references to the result labels so they can be destroyed
# before showing a new route 
label_distance, label_path = None, None


class RouteFrame:
    """
    GUI class handles user interaction related to route planning
    """

    def __init__(self, parent):
        self.parent = parent

    def show_route(self):
        """
        Renders the route planning page
        """
        
        frame = Frame(self.parent, bg='#E6E6E6')
        frame.place(relx=0, rely=0, relheight=1, relwidth=1, anchor='nw')

        #panel for city selection controls
        frame_cities = Frame(frame, bg='#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
        frame_cities.place(relx=0.05, rely=0.05, relheight=0.55, relwidth=0.9, anchor='nw')

        #panel for route results
        frame_route = Frame(frame, bg='#E6E6E6', highlightbackground="#8E8E8E", highlightthickness=1)
        frame_route.place(relx=0.05, rely=0.65, relheight=0.3, relwidth=0.9, anchor='nw')

        
        Label(frame_cities, text='Finding the closest route and distance between\ncities for transportation',  bg = '#E6E6E6', font=("Arial", 13)).place(relx=0.3, rely=0.1)

        Label(frame_cities, text='From: ', bg = '#E6E6E6', font=("Arial", 12)).place(relx=0.1, rely=0.3)
        Label(frame_cities, text='Towards: ', bg = '#E6E6E6', font=("Arial", 12)).place(relx=0.1, rely=0.6)

        #dropdowns created from the cities graph
        city_from = ttk.Combobox(frame_cities, values=return_cities(), state='readonly')
        city_from.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1, anchor='nw')
        city_from.current(0)

        city_to = ttk.Combobox(frame_cities, values=return_cities(), state='readonly')
        city_to.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1, anchor='nw')
        city_to.current(0)

        def show():
            """
            Shows the shortest path and distance between two cities
            """

            global label_distance, label_path

            if label_distance:
                label_distance.destroy()
            if label_path:
                label_path.destroy()

            #destroy previous result labels before rendering new ones
            if city_from.get() == city_to.get():
                messagebox.showerror("Route", "Choose different cities!")
                return
            result = dijkstra(graph, city_from.get(), city_to.get())  #run the algorithm
            if result == 'Path not reachable': 
                messagebox.showerror("Route", "Path not reachable")
                return
            
            #render result strings inside the result panel
            distance, path = result
            distance_text = "Distance between cities: " + str(distance) 
            path_text = "\nPath: " + ' ---> '.join(path)

            label_distance = Label(frame_route, text=distance_text, bg = '#E6E6E6', font=("Arial", 12))
            label_distance.place(relx=0.1, rely=0.3)
            label_path = Label(frame_route, text=path_text, bg = '#E6E6E6', font=("Arial", 12), wraplength=600)
            label_path.place(relx=0.1, rely=0.5)

        def back():  #close the route overlay
            global label_distance, label_path
            label_distance, label_path = None, None
            frame.destroy()
        
        # --- Action buttons ---
        btn_show = Button(frame_cities, text="Show Route", command=show)
        btn_show.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.1, anchor='nw')

        btn_back = Button(frame_cities, text="Back", command=back)
        btn_back.place(relx=0.6, rely=0.7, relwidth=0.2, relheight=0.1, anchor='nw')
