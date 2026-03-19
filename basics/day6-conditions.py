# Day 6 - Conditions (if / else)

# basic if
age = 18

if age >= 18:
    print("Adult")


# if + else
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# if + elif + else
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")


# loop + condition (print even numbers)
for i in range(10):
    if i % 2 == 0:
        print(i)


# filter even numbers from list
numbers = [1, 2, 3, 4, 5]

result = []

for n in numbers:
    if n % 2 == 0:
        result.append(n)

print(result)


# function: filter even numbers
def filter_even(numbers):
    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n)

    return result


print(filter_even([1, 2, 3, 4, 5]))


# function: filter numbers > 15
def filter_greater(numbers):
    result = []

    for n in numbers:
        if n > 15:
            result.append(n)

    return result


print(filter_greater([10, 15, 20, 25]))
