n = int(input("Enter the number : "))
fibonacci_series = []
a,b = 0,1

for i in range (1, n+1):
    fibonacci_series.append(a)
    next = a + b
    a = b
    b = next

print(f"The fibonacci series : {fibonacci_series}")