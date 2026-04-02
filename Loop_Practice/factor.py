n = int(input("Enter the number : "))
factors = []
factors_count = 0

for i in range(1, n+1):
    if(n % i == 0):
        factors.append(i)
        factors_count += 1

print(f"The factors of that number : {factors}")
print(f"The count of factors of that number : {factors_count}")

