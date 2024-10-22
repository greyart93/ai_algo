from queue import PriorityQueue

# Heuristic distances for each node
H_dist = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0,
}

# Graph representation
Graph_nodes = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': None
}

def recursive_best_first_search(graph, current_node, target, visited, current_cost, parent):
    # Base case: if we reach the target
    if current_node == target:
        path = []
        while current_node is not None:
            path.append(current_node)
            current_node = parent[current_node]
        path.reverse()

        print(f"Optimal path: {' -> '.join(path)}")
        print(f"Total cost: {current_cost}")
        return True

    visited.add(current_node)

    # Create a list of neighbors with their costs
    neighbors = graph.get(current_node, [])

    # Sort neighbors based on heuristic cost
    neighbors.sort(key=lambda x: (current_cost + x[1] + H_dist[x[0]]))

    # Explore neighbors
    for neighbor, cost in neighbors:
        if neighbor not in visited:
            parent[neighbor] = current_node
            total_cost = current_cost + cost

            # Recursive call
            if recursive_best_first_search(graph, neighbor, target, visited, total_cost, parent):
                return True

            # Backtrack
            del parent[neighbor]

    return False

def best_first_search(graph, source, target):
    visited = set()  # To keep track of visited nodes
    parent = {source: None}  # To reconstruct the path
    recursive_best_first_search(graph, source, target, visited, 0, parent)

best_first_search(Graph_nodes, 'S', 'G')
