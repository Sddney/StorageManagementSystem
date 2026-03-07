import json

with open("algorithm/cities.json") as f:
    graph = json.load(f)

#Example dataset was taken from kaggle  https://www.kaggle.com/datasets/lightningforpython/russian-cities-distance-dataset

def Dijkstra(graph, start, end):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = dict(graph)
    infinity = float('infinity')
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode]:
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            return 'Path not reachable'
    path.insert(0, start)
    if shortest_distance[end] != infinity:
        return str(shortest_distance[end]), path
    

def ReturnCities():
    with open("algorithm/cities.json") as f:
        data = json.load(f)
    return list(dict(data).keys())
    


#print(Dijkstra(graph, "Blagodarnyy", "Budonnovsk"))