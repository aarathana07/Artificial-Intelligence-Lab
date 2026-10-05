states = [(3, 3, 1)]
parent = {}

i = 0

while i < len(states):

    m, c, boat = states[i]
    i = i + 1

    for x in range(3):
        for y in range(3):

            if x + y >= 1 and x + y <= 2:

                if boat == 1:
                    nm = m - x
                    nc = c - y
                    nb = 0
                else:
                    nm = m + x
                    nc = c + y
                    nb = 1

                if nm >= 0 and nc >= 0 and nm <= 3 and nc <= 3:

                    if (nm == 0 or nm >= nc) and (3-nm == 0 or 3-nm >= 3-nc):

                        new = (nm, nc, nb)

                        if new not in states:
                            states.append(new)
                            parent[new] = (m, c, boat)

    if (0, 0, 0) in states:
        break

current = (0, 0, 0)
path = []

while current != (3, 3, 1):
    path.append(current)
    current = parent[current]

path.append((3, 3, 1))
path.reverse()

print("Solution:")

for x in path:
    print(x)
