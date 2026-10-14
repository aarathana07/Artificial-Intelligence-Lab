
def alphabeta(tree, alpha, beta, maximizing):
    if not isinstance(tree, list):
        return tree

    if maximizing:
        value = float("-inf")

        for child in tree:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float("inf")

        for child in tree:
            value = min(value, alphabeta(child, alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value

tree = [[3, 5, 2], [9, 1, 4], [6, 7, 8]]

score = alphabeta(tree, float("-inf"), float("inf"), True)

print("Best score:", score)
