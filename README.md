# recursive_best-first_search

This code implements the Best-First Search (BFS) algorithm to find the optimal path from a given source node to a target node in a graph. Here's a detailed explanation of the code:

Imports:

from queue import PriorityQueue: This line imports the PriorityQueue class from the queue module, which is used to maintain the priority queue during the search.
Heuristic Distances (H_dist):

This dictionary stores the heuristic distances (estimated costs) for each node in the graph. The heuristic distance is used to guide the search towards the target node.
Graph Representation (Graph_nodes):

This dictionary represents the graph, where each key is a node, and the value is a list of its neighboring nodes and their corresponding costs.
Recursive Best-First Search (recursive_best_first_search):

This function implements the recursive version of the Best-First Search algorithm.
Parameters:
graph: The graph representation.
current_node: The current node being explored.
target: The target node to be reached.
visited: A set of visited nodes to avoid revisiting them.
current_cost: The current cost of the path from the source to the current node.
parent: A dictionary to keep track of the parent of each node in the path.
Base case: If the current node is the target node, the function reconstructs the optimal path, prints it, and the total cost, and returns True.
Recursive case:
The function adds the current node to the visited set.
It retrieves the list of neighbors for the current node from the graph.
The neighbors are sorted based on the sum of the current cost, the cost to reach the neighbor, and the heuristic distance to the target.
The function recursively explores each unvisited neighbor, updating the parent dictionary and the total cost.
If the recursive call returns True, the function returns True to indicate that the target has been found.
If the recursive call returns False, the function backtracks by removing the neighbor from the parent dictionary.
The function returns False if the target node is not found.
Best-First Search (best_first_search):

This function is the entry point for the Best-First Search algorithm.
Parameters:
graph: The graph representation.
source: The source node.
target: The target node.
The function initializes the visited set and the parent dictionary, with the source node as the root.
It calls the recursive_best_first_search function with the initial parameters and starts the search.
Execution:

The code calls the best_first_search function with the Graph_nodes graph, the source node 'S', and the target node 'G'.
The Best-First Search algorithm is a heuristic-based search algorithm that explores the graph by always selecting the node that appears to be closest to the target based on the heuristic function (the H_dist dictionary in this case). The algorithm continues to explore the graph until it finds the target node or exhausts all possible paths.
