import heapq
def a_star_directed_weighted_user(graph, start, goal, heuristic):
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
# Input directed weighted graph and heuristic values from user
graph = {}
heuristic = {}
num_edges = int(input("Enter number of edges: "))
for _ in range(num_edges):
    u, v, cost = input("Enter edge (u v cost): ").split()
    cost = float(cost)
    graph.setdefault(u, []).append((v, cost))
    # No reverse edge since it's directed
nodes = set()
for node in graph:
   nodes.add(node)
    for neighbor, _ in graph[node]:
        nodes.add(neighbor)
for node in nodes:
    heuristic[node] = float(input(f"Enter heuristic value for {node}: "))
# Perform A* Search
start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")
a_star_directed_weighted_user(graph, start_node, goal_node, heuristic)
