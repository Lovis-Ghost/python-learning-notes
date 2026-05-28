# Day 6 - Python Conditions / Python 条件判断

# What I learned / 我学到了什么
# - Use if / 使用 if
# - Use else and elif / 使用 else 和 elif
# - Combine loops and conditions / 结合循环和条件

# Simple Chinese explanation / 简单中文解释
# condition 可以让程序根据不同情况做不同事情。常见写法是 if, elif, else。

# Short English summary
# Conditions help Python make simple decisions.

# Beginner-friendly code example / 入门代码例子
age = 18

if age >= 18:
    print("Adult")

student_age = 16

if student_age >= 18:
    print("Adult")
else:
    print("Minor")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

for number in range(10):
    if number % 2 == 0:
        print("Even number:", number)

numbers = [1, 2, 3, 4, 5]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers:", even_numbers)


def filter_even_numbers(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


print(filter_even_numbers([1, 2, 3, 4, 5]))


def filter_greater_than_fifteen(numbers):
    result = []

    for number in numbers:
        if number > 15:
            result.append(number)

    return result


print(filter_greater_than_fifteen([10, 15, 20, 25]))

# Common mistakes / 常见错误
# 1. Using = instead of == when comparing values.
# 2. Forgetting the colon after if, elif, or else.
# 3. Forgetting indentation under the condition.

# Practice questions / 练习题
# 1. Check if a number is positive.
# 2. Check if a score is pass or fail.
# 3. Print only numbers greater than 10 from a list.
