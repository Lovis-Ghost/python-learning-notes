# day5-loops.py

# 1 basic loop
for i in range(5):
    print(i)


# 2 list loop
numbers = [10, 20, 30]

for n in numbers:
    print(n)


# 3 multiply
numbers = [1, 2, 3]

for n in numbers:
    print(n * 2)


# 4 function + loop
def double(x):
    return x * 2

numbers = [2, 4, 6]

for n in numbers:
    print(double(n))


# 5 sum
numbers = [1, 2, 3, 4]

total = 0

for n in numbers:
    total = total + n

print(total)
