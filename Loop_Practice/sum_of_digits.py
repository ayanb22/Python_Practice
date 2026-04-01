n = int(input("Enter the number : "))
total = 0

while n > 0 :
    remainder = n % 10
    total += remainder
    n = n // 10

print(f"The sum of the number : {total}")

