highest_range = int(input("Enter the range : "))
number_list = []
unique_digits = []
i = 1
while i <= highest_range:
    number_list.append(int(input("Enter the numbers : ")))
    i += 1


for number in number_list:
    found = False
    for digit in unique_digits:
        if number == digit:
            found = True
            break
    if not found:
        unique_digits.append(number)



print(unique_digits)