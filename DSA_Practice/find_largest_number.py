def largest_number(n):
    input_list = []
    
    i = 1
    
    while i <= n:
        number = int(input("Enter the number you want to add in the list : "))
        input_list.append(number)
        i += 1

    maximum_number = input_list[0]

    for number in input_list:
        if number > maximum_number:
            maximum_number = number

    return maximum_number


number = int(input("Enter the number of elements will be in the list : "))
print(largest_number(number))