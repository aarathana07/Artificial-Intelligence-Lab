
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)

        for next_node in graph[node]:
            dfs(next_node)

dfs('A')

print("DFS Traversal:", visited)
