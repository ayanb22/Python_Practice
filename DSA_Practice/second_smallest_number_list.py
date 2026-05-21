def smallest_number_in_list(n):
    input_list = []
    i = 1
    
    while i <= n:
        number = int(input("Enter the number you want to add in the list : "))
        input_list.append(number)
        i += 1
    
    input_list.sort()
    smallest_number = input_list[0]

    for number in input_list:
        if smallest_number < number:
            smallest_number = number
            break
        
    if smallest_number == input_list[0]:
        smallest_number = 0
    return smallest_number

number = int(input("Enter the number of elements will be in the list : "))
result = smallest_number_in_list(number)
if result == 0:
    print("There is no 2nd smallest number")
else:
    print(result)

