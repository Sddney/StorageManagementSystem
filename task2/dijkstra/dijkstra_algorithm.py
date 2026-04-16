import json
import copy

#Dataset source: https://www.kaggle.com/datasets/lightningforpython/russian-cities-distance-dataset

def dijkstra(graph, start, end):

    """
    Dijkstra's algorithm implementation to find the shortest path between two cities.

    Args:
        graph (dict): A dictionary representing the graph of cities and distances.
        start (str): The starting city.
        end (str): The destination city.

    Returns:
        tuple: A tuple containing the shortest distance and the path as a list of cities.
                If no path is found, returns 'Path not reachable'.

    """

    shortest_distance = {}  
    predecessor = {}
    unseen_nodes = copy.deepcopy(graph)
    infinity = float('infinity')
    path = []

    #initialize all distances as infinity
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    #visiting all nodes and finding node with minimum distance
    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        #check distances to neighboring nodes and update shortest distance if new distance is shorter
        for childNode, weight in graph[min_node]:
            if weight + shortest_distance[min_node] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[min_node]
                predecessor[childNode] = min_node
        unseen_nodes.pop(min_node)

    #path from end to start
    current_node = end
    while current_node != start:
        try:
            path.append(current_node)
            current_node = predecessor[current_node]
        except KeyError:
            return 'Path not reachable'  #if no path exists
    path.append(start)
    path.reverse()
    if shortest_distance[end] != infinity:
        return shortest_distance[end], path


def return_cities():

    """
    Returns a list of all cities in the dataset.

    Used for dropdown menus in GUI

    """

    with open("task2/dijkstra/cities.json") as f:
        data = json.load(f)
    return list(dict(data).keys())
    


    

