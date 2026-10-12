
rooms = {"A": 1, "B": 1}

print("Initial State:", rooms)

for room in rooms:
    if rooms[room] == 1:
        print("Room", room, "is Dirty")
        rooms[room] = 0
        print("Room", room, "is Clean")

print("Final State:", rooms)
