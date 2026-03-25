from tkinter import *
from tkinter import messagebox, ttk

from algorithm.dijkstra_algorithm import Dijkstra, ReturnCities
import json

with open("algorithm/cities.json") as f:
        graph = json.load(f)


label_distance, label_path = None, None


class RouteFrame():

    def __init__(self, parent):
        self.parent = parent

    def show_route(self):
        
        frame = Frame(self.parent, bg='#E6E6E6')
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

        btn_back = Button(frame_cities, text="Back", command=Back)
        btn_back.place(relx=0.6, rely=0.7, relwidth=0.2, relheight=0.1, anchor='nw')
