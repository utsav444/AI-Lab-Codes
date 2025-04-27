import heapq
import pandas as pd
def a_star_undirected_weighted_csv(graph, start, goal, heuristic):
    priority_queue = [(0 + heuristic[start], 0, start)]  # (f(n), g(n), node)
    visited = set()
    while priority_queue:
        f_n, g_n, node = heapq.heappop(priority_queue)
        if node == goal:
            print(f"Found goal: {goal}")
            return
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (g_n + cost + heuristic[neighbor], g_n + cost, neighbor))
# Read undirected weighted graph and heuristic from CSV
df_edges = pd.read_csv('graph_edges.csv', header=None)  # columns: source, target, weight
df_heuristic = pd.read_csv('heuristic.csv', header=None)  # columns: node, heuristic_value
graph = {}
heuristic = {}
for row in df_edges.values:
    u, v, weight = row
    weight = float(weight)
    graph.setdefault(u, []).append((v, weight))
    graph.setdefault(v, []).append((u, weight))  # Add reverse edge for undirected
for row in df_heuristic.values:
    node, h_value = row
    heuristic[node] = float(h_value)
# Perform A* Search
start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")
a_star_undirected_weighted_csv(graph, start_node, goal_node, heuristic)
