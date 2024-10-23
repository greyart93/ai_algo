# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['G'],
#     'D': [],
#     'E': ['F'],
#     'G': [],
#     'F': []
# }


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'K', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

'''
graph representation:
 
                                  A 
                               /    \
                             B        C 
                            / \     / | \
                           D    E  F  |  G
                          / \  / \    |
                         H   I J  K---|

'''

def DFS(currentNode, destination, graph, maxDepth, path):
    path.append(currentNode)  # Add current node to the path
    # print("Current Node: ", currentNode)
    
    if currentNode == destination:
        return True, path  # Return True and the current path
    
    if maxDepth <= 0:
        path.pop()  # Remove the current node before backtracking
        return False, path
    
    for node in graph[currentNode]:
        found, resultPath = DFS(node, destination, graph, maxDepth - 1, path)
        if found:
            return True, resultPath  # If found, return True and the path
    
    path.pop()  # Remove the current node before backtracking
    return False, path

def IDFS(currentNode, destination, graph, maxDepth):
    for i in range(maxDepth):
        found, resultPath = DFS(currentNode, destination, graph, i, [])
        if found:  # If a path is found
            return resultPath  # Return the shortest path
    return None  # No path found

# Driver code to find and print the shortest path
shortest_path = IDFS('A', 'K', graph, 4)
if shortest_path is None:
    print("Path is not available")
else:
    print("IDFS: Shortest path from A to K:", " -> ".join(shortest_path))
