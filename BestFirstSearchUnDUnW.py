import heapq
def best_first_search_undirected_unweighted(graph, start, heuristic):
    priority_queue = [(heuristic[start], start)]
    visited = set()
    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                  # Input undirected unweighted graph and heuristic values from user
graph = {}
heuristic = {}
num_edges = int(input("Enter number of edges: "))
for _ in range(num_edges):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)  # Add reverse edge for undirected
nodes = set(graph.keys())
for node in nodes:
    heuristic[node] = float(input(f"Enter heuristic value for {node}: "))
# Perform Best First Search
start_node = input("Enter start node: ")
best_first_search_undirected_unweighted(graph, start_node, heuristic)
