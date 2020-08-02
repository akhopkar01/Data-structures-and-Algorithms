from collections import defaultdict
import numpy as np

class Graph:
    def __init__(self):
        self.nodes = set()  # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(
            list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance  # lets make the graph undirected / bidirectional

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)


def dijkstra(graph, source):
    # Declare and initialize result, unvisited, and path
    result = {}
    result[source] = 0
    for node in graph.nodes:
        if node != source:
            result[node] = np.inf

    unvisited = set(graph.nodes)
    path = {}
    # As long as unvisited is non-empty
    while unvisited:
        max_node = None
        # 1. Find the unvisited node having smallest known distance from the source node.
        for node in unvisited:
            if node in result:
                if max_node is None:
                    max_node = node
                elif result[node] < result[max_node]:
                    max_node = node
        if max_node is None:
            break

        current_distance = result[max_node]

        # 2. For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[max_node]:
            if neighbour in unvisited:
                dist = current_distance + graph.distances[(max_node, neighbour)]

                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.
                if neighbour not in result or dist < result[neighbour]:
                    result[neighbour] = dist
                    # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                    path[neighbour] = max_node
        # 5. Remove the current node from the unvisited set.
        unvisited.remove(max_node)

    return result


# Test 1
testGraph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A','B',3)
testGraph.add_edge('A','D',2)
testGraph.add_edge('B','D',4)
testGraph.add_edge('B','E',6)
testGraph.add_edge('B','C',1)
testGraph.add_edge('C','E',2)
testGraph.add_edge('E','D',1)

print(dijkstra(testGraph, 'A'))     # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}

