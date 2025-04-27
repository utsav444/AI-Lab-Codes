def dfs_non_recursive(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            # Add neighbors in reverse order to maintain left-to-right traversal
            stack.extend(reversed(graph[node]))
# Input graph from user
graph = {}
num_edges = int(input("Enter number of edges: "))
for _ in range(num_edges):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
# Perform DFS
start_node = input("Enter start node: ")
dfs_non_recursive(graph, start_node)

