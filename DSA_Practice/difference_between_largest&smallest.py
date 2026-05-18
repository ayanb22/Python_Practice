def difference_between_largest_smallest(n):
    input_list = []
    i = 1
    
    while i <= n:
        number = int(input("Enter the number you want to add in the list : "))
        input_list.append(number)
        i += 1

    largest_number = input_list[0]
    smallest_number = input_list[0]
    
    for digit in input_list:
        if digit > largest_number:
            largest_number = digit
        if  digit < smallest_number:
            smallest_number = digit

    difference = largest_number - smallest_number

    return difference

number = int(input("Enter the number of elements will be in the list : "))
print(difference_between_largest_smallest(number))

