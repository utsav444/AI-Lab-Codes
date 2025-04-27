import pandas as pd

def dfs_recursive(graph, node, visited):
    visited.add(node)
    print(node, end=" ")  # Process the node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
# Read graph from CSV
df = pd.read_csv('D:\AI Lab\Codes\graph.csv', header=None)
graph = {}
for row in df.values:
    u, v = row
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
# Perform DFS
start_node = list(graph.keys())[0]  # Start from the first node
visited = set()
dfs_recursive(graph, start_node, visited)
