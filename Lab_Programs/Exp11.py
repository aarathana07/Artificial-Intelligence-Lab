
board = [" "] * 9

def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def winner(mark):
    lines = [(0,1,2),(3,4,5),(6,7,8),
             (0,3,6),(1,4,7),(2,5,8),
             (0,4,8),(2,4,6)]
    return any(all(board[i] == mark for i in line)
               for line in lines)

player = "X"
turn = 0

while turn < 9:
    show()
    pos = int(input(player + ", position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position. Try again.")
        continue

    board[pos] = player
    turn += 1

    if winner(player):
        show()
        print(player, "wins!")
        break

    player = "O" if player == "X" else "X"
else:
    show()
    print("It's a draw!")
