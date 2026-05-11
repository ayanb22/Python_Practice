def duplicate_element(n):
    input_list = []
    seen_list = []
    duplicate_list = []
    i = 1

    while i <= n:
        number_input = int(input("Enter the number you want to add in the list : "))
        input_list.append(number_input)
        i += 1
        

    for number in input_list:
        if number in seen_list:
            if number not in duplicate_list:
                duplicate_list.append(number)
        else:
            seen_list.append(number)

    return duplicate_list


number = int(input("Enter the number of elements in the list : "))
print(duplicate_element(number))


