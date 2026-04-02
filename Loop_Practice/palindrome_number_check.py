n = int(input("Enter the number : "))
original_number = n
revese_number = 0

while n > 0:
    remainder = n % 10
    revese_number = (revese_number * 10) + remainder
    n = n // 10

if(revese_number == original_number):
    print(f"The number is palindrome")
else:
    print(f"The number is not palindrome")
