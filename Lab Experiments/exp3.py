a = 0
b = 0

print("Jug 1 = 4 litres")
print("Jug 2 = 3 litres")
print("Goal = 2 litres")

while a != 2 and b != 2:

    print("\n1. Fill Jug 1")
    print("2. Fill Jug 2")
    print("3. Empty Jug 1")
    print("4. Empty Jug 2")
    print("5. Pour Jug 1 into Jug 2")
    print("6. Pour Jug 2 into Jug 1")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a = 4

    elif choice == 2:
        b = 3

    elif choice == 3:
        a = 0

    elif choice == 4:
        b = 0

    elif choice == 5:
        x = min(a, 3 - b)
        a = a - x
        b = b + x

    elif choice == 6:
        x = min(b, 4 - a)
        b = b - x
        a = a + x

    else:
        print("Invalid choice")

    print("Jug 1 =", a, "litres")
    print("Jug 2 =", b, "litres")

print("\nGoal Reached!")
