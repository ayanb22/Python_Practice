n = int(input("Enter the number : "))
even_digits = []
odd_digits = []
even_number = 0
odd_number = 0

while n > 0:
    remainder = n % 10
    if(remainder % 2 == 0):
        even_number += 1
        even_digits.append(remainder)
    else:
        odd_number += 1
        odd_digits.append(remainder)
    n = n // 10

print(f"The even integers are : {even_digits}")
print(f"The count of even numbers : {even_number}")
print(f"The odd integers are : {odd_digits}")
print(f"The count of odd numbers : {odd_number}")