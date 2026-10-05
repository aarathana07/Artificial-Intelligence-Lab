p = [1, 2, 3, 4, 0, 6, 7, 5, 8]

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print("Initial:")
print(p[0], p[1], p[2])
print(p[3], p[4], p[5])
print(p[6], p[7], p[8])

while p != goal:

    pos = p.index(0)

    print("\n0 = Blank")
    print("1. Up")
    print("2. Down")
    print("3. Left")
    print("4. Right")

    choice = int(input("Enter move: "))

    if choice == 1 and pos >= 3:
        p[pos], p[pos-3] = p[pos-3], p[pos]

    elif choice == 2 and pos < 6:
        p[pos], p[pos+3] = p[pos+3], p[pos]

    elif choice == 3 and pos % 3 != 0:
        p[pos], p[pos-1] = p[pos-1], p[pos]

    elif choice == 4 and pos % 3 != 2:
        p[pos], p[pos+1] = p[pos+1], p[pos]

    else:
        print("Invalid move")
        continue

    print("\nPuzzle:")
    print(p[0], p[1], p[2])
    print(p[3], p[4], p[5])
    print(p[6], p[7], p[8])

print("\nPuzzle Solved!")
