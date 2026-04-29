def first_non_repeating(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in s:
        if char_count[char] == 1:
            return char

    return None


s = input("Enter The string you want to check : ")
print(first_non_repeating(s))