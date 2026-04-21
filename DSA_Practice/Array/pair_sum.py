def pair_sum(n, m):
    sum_digit = []
    
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == m:
                sum_digit.append((n[i], n[j]))
    
    return sum_digit


# Input section
digits = []
count = int(input("Enter length of the numbers: "))

for _ in range(count):
    digits.append(int(input("Enter the number: ")))

target = int(input("Enter the sum: "))

print(pair_sum(digits, target))

