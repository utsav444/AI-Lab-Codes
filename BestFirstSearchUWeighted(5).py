import heapq
def best_first_search_undirected_weighted(graph, start, heuristic):
    priority_queue = [(heuristic[start], start)]
    visited = set()
    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
# Input undirected weighted graph and heuristic values from user
graph = {}
heuristic = {}
num_edges = int(input("Enter number of edges: "))
for _ in range(num_edges):
    u, v, weight = input("Enter edge (u v weight): ").split()
    weight = float(weight)
    graph.setdefault(u, []).append((v, weight))
    graph.setdefault(v, []).append((u, weight))  # Add reverse edge for undirected
nodes = set()
for node in graph:
    nodes.add(node)
    for neighbor, _ in graph[node]:
        nodes.add(neighbor)
for node in nodes:
    heuristic[node] = float(input(f"Enter heuristic value for {node}: "))
# Perform Best First Search
start_node = input("Enter start node: ")
best_first_search_undirected_weighted(graph, start_node, heuristic)
