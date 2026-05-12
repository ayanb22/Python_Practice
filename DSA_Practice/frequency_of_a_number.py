def frequency_count(n):
    input_list = []
    frequency_dict = {}
    i = 1

    while i <= n:
        number = int(input("Enter the number : "))
        input_list.append(number)
        i += 1

    for element in input_list:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    return frequency_dict


number = int(input("Enter the number of elements in the list : "))
print(frequency_count(number))