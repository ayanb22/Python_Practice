n = int(input("Enter the number : "))
digits_length = []
a,b = 0,1

for i in range (1, n+1):
    digits_length.append(a)
    next = a + b
    a = b
    b = next

print(f"The fibonacci series : {digits_length}")