def find_common_elements(n,m):
    first_list = []
    second_list = []
    i = 1
    j = 1
    duplicate_list = []

    print("------- First List --------")
    while i <= n:
        number = int(input("Enter the number: "))
        first_list.append(number)
        i += 1

    print("------- Second List --------")
    while j <= m:
        number = int(input("Enter the number: "))
        second_list.append(number)
        j += 1

    for element in first_list:
        if element in second_list:
            if element not in duplicate_list:
                duplicate_list.append(element)

    return duplicate_list


first_list_number = int(input("Enter the highest number of element in first list : "))
second_list_number = int(input("Enter the highest number of element in second list : "))

print(find_common_elements(first_list_number,second_list_number))
