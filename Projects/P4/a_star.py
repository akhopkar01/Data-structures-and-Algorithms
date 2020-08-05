import math

class Node:
    def __init__(self, node = None, cost = 0):
        self.node = node
        self.cost = cost

    def __repr__(self):
        return " Node : {}, Cost: {}".format(self.node, self.cost)

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, node, cost):
        self.queue.append(Node(node, cost))
        self.queue = sorted(self.queue, key=lambda x: x.cost)

    def pop(self):
        return self.queue.pop(0)

    def __repr__(self):
        return " {} ".format(self.queue)
        
def heuristic(p1, p2):
    # Euclidean Heuristic is used
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def shortest_path(M, start, target):
    visited_nodes = set() # Keep track of visited node
    queue = PriorityQueue() # priority queue
    
    # Cost matrix initialization - setting to Infinity
    cost_matrix = {}
    for node in M.intersections:
        cost_matrix[node] = math.inf
    cost_matrix[start] = 0
    
    visited_nodes.add(start)
    queue.push(start, cost_matrix[start])
    
    # Path explored initialization
    path = {}
    path[start] = None
    target_found = False
    
    while queue and not target_found:
        node = queue.pop()
        current_node = node.node
        node_cost = node.cost
        
        if current_node == target:
            # Target found, break loop
            target_found = True
        
        visited_nodes.add(current_node)
        
        # Check all neighbours of the road
        for neighbour in M.roads[current_node]:
            if neighbour not in visited_nodes:
                
                old_cost = cost_matrix[neighbour] 
                new_cost = node_cost + heuristic(M.intersections[current_node], M.intersections[neighbour]) # cost to come + cost to go
                
                if new_cost < old_cost:
                    cost_matrix[neighbour] = new_cost # Update cost matrix
                    queue.push(neighbour, new_cost) # push new node to queue
                    path[neighbour] = current_node # update path explored
                    
    
    # Backtrack [goal - start]
    
    final_path = []
    current = target
    while target is not start:
        final_path.append(target)
        target = path[target]
    final_path.append(start)
    
    return final_path[::-1]