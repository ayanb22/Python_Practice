n = int(input("Enter the number : "))
reverse_number = 0

while n > 0:
    remainder = n % 10
    reverse_number = (reverse_number * 10) + remainder
    n = n // 10

print(f"The reverse of that number : {reverse_number}")
