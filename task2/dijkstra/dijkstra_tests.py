import json
import unittest
from dijkstra.dijkstra_algorithm import dijkstra
class TestDijkstra(unittest.TestCase):
    def test_near_cities(self):
        with open("dijkstra/cities.json") as f:
            graph = json.load(f)

        distance, path = dijkstra(graph, "Budonnovsk", "Zelenokumsk")

        assert distance == 60


    def test_dijkstra(self):
        with open("dijkstra/cities.json") as f:
            graph = json.load(f)


        distance, path = dijkstra(graph, "Nevinnomyssk", "Lermontov")

        assert distance == 147