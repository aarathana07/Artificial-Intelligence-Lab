
def sigmoid(x):
    return 1 / (1 + 2.71828 ** (-x))

x = 0.5
w1 = 0.4
b1 = 0.1

hidden = sigmoid(x * w1 + b1)

w2 = 0.6
b2 = 0.2

output = sigmoid(hidden * w2 + b2)

print("Hidden:", round(hidden, 2))
print("Output:", round(output, 2))
