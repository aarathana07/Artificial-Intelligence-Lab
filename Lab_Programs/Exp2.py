n = 8
board = [-1] * n

row = 0

while row < n:

    print("\nBoard:")

    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    col = int(input("Enter column (1-8) for Queen: ")) - 1

    if col < 0 or col >= n:
        print("Invalid position! Try again.")
        continue

    safe = True

    for i in range(row):
        if board[i] == col:
            safe = False

        if abs(board[i] - col) == abs(i - row):
            safe = False

    if safe:
        board[row] = col
        print("Queen placed!")
        row += 1
    else:
        print("Invalid position! Try again.")


print("\nYou solved the 8-Queen problem!")

for i in range(n):
    for j in range(n):
        if board[i] == j:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
