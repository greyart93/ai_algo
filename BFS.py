#bfs for shortest path v1

from collections import deque

def BFS(graph, start, goal): # added goal --added
    visited = []  # list for visited nodes
    queue = deque()    # list for queue
    parent = {}   # add dictionary to track the path  -- added 

    visited.append(start)  # add start node into visited list
    queue.append(start)    # add start node into queue

    while queue:  # while queue is not empty
        n = queue.popleft()  # pop the front node in queue
        print("curr node: ", n)
        
        # added start
        if n == goal:  # check if we reached the goal
            path = [] # list for path
            while n is not None:  # reconstruct the path while n is not empty
                path.append(n)
                n = parent.get(n)
                # print("parent.get(n):", n)
            print(f"BFS: Shortest path from {start} to {goal}: {' -> '.join(reversed(path))}")
            return
        # added end

        for neighbor in graph[n]:  # visit all neighbors of current node
            if neighbor not in visited:  # if neighbor is not visited
                visited.append(neighbor)  # visit the neighbor
                queue.append(neighbor)     # add the neighbor node into queue
                parent[neighbor] = n       # added set parent for path reconstruction -- added

    print(f"BFS: {goal} not found") # -- added 


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'K'],
    'D': ['B', 'H', 'I'],
    'E': ['B', 'J', 'K'],
    'F': ['C', 'K'],
    'G': ['C'],
    'H': ['D'],
    'I': ['D'],
    'J': ['E'],
    'K': ['E']
}

'''
graph representation:
                                A 
                            /       \
                          B           C 
                         /    \      / |  \
                        D      E    F  |   G
                      / \    / \      |
                      H  I   J  K  -----


'''

# Run BFS
# BFS(graph, "A", "K")


'''
- add goal parameter in bfs function, this is the goal node i.e. destination
- add a dictionary named parent to track the path to get the Shortest path
- after printing n do:
- check if n is goal node 
- if yes then: 
- create a list named path
- and inside if do a while loop as while n is not none:
- append n to path list
- update n value to its parent node by using parent dict with n as key , cuz it reversed the dict, i.e. neighbor: curr node 
- print(f"BFS: Shortest path from {start} to {goal}: {' -> '.join(reversed(path))}") and return 

- parent dict work in short:
p = {}  # init a dict
p["k"] = "c"  # p[neighbor] = n i.e. curr node , so P { K: "C" }
r = p.get("k") # get() -> returns the value of the given key
print(r) 

- if neighbor not in visited: code add parent[neighbor] = n 

'''

# # bfs for path v1 but lazy code:

graph2 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G', 'K'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []

}


def bfs2(g, s, e):
    v = set(s)
    q = [s]
    parent = {}
    
    while q:
        n = q.pop(0)
        print(n)
        
        if n == e:
            path = []
            while n:
                path.append(n)
                n = parent.get(n)
            print(f"BFS: SP from {s} to {e}: { '->'.join(reversed(path))}")
            return
        
        for i in g[n]:
            if i not in v:
                v.add(i)
                q.append(i)
                parent[i] = n
    
    print(f'{e} not found')
    
            
    
bfs2(graph2, 'A', 'J')
print("\n\n")




