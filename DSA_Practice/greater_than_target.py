def greater_than_target(n):
    input_list = []
    output_list = []
    i = 1
    
    while i <= n:
        number = int(input("Enter the number you want to add in the list : "))
        input_list.append(number)
        i += 1

    target = int(input("Enter the target number : "))

    for number in input_list:
        if number > target:
            output_list.append(number)

    return output_list


number = int(input("Enter the number of elements will be in the list : "))
result = greater_than_target(number)
if not result:
    print("There is no number in the list greater than the target number")
else:
    print(result)