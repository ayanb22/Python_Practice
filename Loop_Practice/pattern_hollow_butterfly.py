n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, 2 * n + 1):
        if j <= i or j > (2 * n - i):
            if j == 1 or j == i or j == (2 * n - i + 1) or j == 2 * n:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")
    print()

for i in range(n, 0, -1):
    for j in range(1, 2 * n + 1):
        if j <= i or j > (2 * n - i):
            if j == 1 or j == i or j == (2 * n - i + 1) or j == 2 * n:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")
    print()