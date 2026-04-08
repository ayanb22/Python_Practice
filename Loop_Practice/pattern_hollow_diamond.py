n = int(input("Enter the diamond size : "))

for i in range(1, n+1):
    for j in range(n-i, 0, -1):
        print(" ", end=" ")
    for k in range(2*i-1, 0, -1):
        if(k==1 or k == 2*i-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n-1, 0, -1):
    for j in range(n-i, 0, -1):
        print(" ", end=" ")
    for k in range(2*i-1, 0, -1):
        if(k==1 or k==2*i-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
