import json
import copy

#Dataset source: https://www.kaggle.com/datasets/lightningforpython/russian-cities-distance-dataset
with open("algorithm/cities.json") as f:
    graph = json.load(f)


def Dijkstra(graph, start, end):

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
    unseenNodes = copy.deepcopy(graph)
    infinity = float('infinity')
    path = []

    #initialize all distances as infinity
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    #visiting all nodes and finding node with minimum distance
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        #check distances to neighboring nodes and update shortest distance if new distance is shorter
        for childNode, weight in graph[minNode]:  
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:  
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    #path from end to start
    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            return 'Path not reachable'  #if no path exists
    path.insert(0, start)
    if shortest_distance[end] != infinity:
        return str(shortest_distance[end]), path
    

def ReturnCities():

    """
    Returns a list of all cities in the dataset.

    Used for dropdown menus in GUI

    """

    with open("algorithm/cities.json") as f:
        data = json.load(f)
    return list(dict(data).keys())
    

