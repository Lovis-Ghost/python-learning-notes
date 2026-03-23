# Day 7 - Advanced Conditions (and / or)

# 1️⃣ basic AND condition
n = 12

if n % 2 == 0 and n > 10:
    print("Even and >10")


# 2️⃣ basic OR condition
n = 3

if n == 0 or n == 1:
    print("Small number")


# 3️⃣ loop + AND condition
for i in range(21):
    if i % 2 == 0 and i > 10:
        print(i)


# 4️⃣ filter list with AND
numbers = [5, 12, 18, 7, 20, 3]

result = []

for n in numbers:
    if n % 2 == 0 and n > 10:
        result.append(n)

print(result)


# 5️⃣ function: filter even and >10
def filter_even_gt10(numbers):
    result = []

    for n in numbers:
        if n % 2 == 0 and n > 10:
            result.append(n)

    return result


print(filter_even_gt10([5, 12, 18, 7, 20, 3]))


# 6️⃣ function: OR condition
def filter_special(numbers):
    result = []

    for n in numbers:
        if n < 5 or n > 15:
            result.append(n)

    return result


print(filter_special([2, 6, 10, 20]))


# 7️⃣ function: range filter 
def filter_range(numbers):
    result = []

    for n in numbers:
        if n >= 10 and n <= 20:
            result.append(n)

    return result


print(filter_range([5, 10, 15, 25]))
