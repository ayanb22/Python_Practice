def main(n):
    input_list = []
    positive_digit = []
    positive_count = 0
    negative_digit = []
    negative_count = 0
    i = 1

    while i <= n:
        number_input = int(input("Enter the number you want to add in the list : "))
        input_list.append(number_input)
        i += 1

    for number in input_list:
        if number > 0:
            positive_digit.append(number)
            positive_count += 1
        elif number < 0:
            negative_digit.append(number)
            negative_count += 1

    return positive_digit, positive_count, negative_digit, negative_count


number = int(input("Enter the number of elements in the list : "))
positive_digit, positive_count, negative_digit, negative_count = main(number)

print(f"The Positive Integers : {positive_digit}")
print(f"The Count of Positive Integers : {positive_count}")
print(f"The Negative Integers : {negative_digit}")
print(f"The Count of Negative Integers : {negative_count}")
