
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 2, 'B': 1, 'C': 1, 'D': 0}

open_list = [(h['A'], 0, 'A', ['A'])]
visited = []

while open_list:
    open_list.sort()
    f, g, node, path = open_list.pop(0)

    if node == 'D':
        print("Shortest Path:", path)
        print("Total Cost:", g)
        break

    if node not in visited:
        visited.append(node)

        for next_node, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[next_node]
            open_list.append(
                (new_f, new_g, next_node, path + [next_node])
            )
