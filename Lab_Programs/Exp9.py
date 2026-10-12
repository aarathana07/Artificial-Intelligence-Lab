
from itertools import permutations

cities = ['A', 'B', 'C']

distance = {
    ('A', 'B'): 10, ('A', 'C'): 15,
    ('B', 'A'): 10, ('B', 'C'): 20,
    ('C', 'A'): 15, ('C', 'B'): 20
}

shortest = None
min_cost = float('inf')

for route in permutations(cities[1:]):
    path = ['A'] + list(route) + ['A']
    cost = 0

    for i in range(len(path) - 1):
        cost += distance[(path[i], path[i + 1])]

    if cost < min_cost:
        min_cost = cost
        shortest = path

print("Shortest Route:", shortest)
print("Minimum Cost:", min_cost)
