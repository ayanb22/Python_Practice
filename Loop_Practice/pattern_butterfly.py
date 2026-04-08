n = int(input("Enter the size of the butterfly : "))


for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    for k in range(2*(n-i)):
        print(" ", end=" ")
    for l in range(1, i+1):
        print("*", end=" ")
    print()

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    for k in range(2*(n-i)):
        print(" ", end=" ")
    for l in range(i, 0, -1):
        print("*", end=" ")
    print()