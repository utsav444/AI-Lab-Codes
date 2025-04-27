from collections import deque
def bfs(graph, start):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
# Input graph from user
graph = {}
num_edges = int(input("Enter number of edges: "))
for _ in range(num_edges):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
# Perform BFS
start_node = input("Enter start node: ")
bfs(graph, start_node)
