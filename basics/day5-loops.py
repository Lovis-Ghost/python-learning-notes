# Day 5 - Python Loops / Python 循环

# What I learned / 我学到了什么
# - Use for loops / 使用 for 循环
# - Loop through a list / 遍历列表
# - Use a loop to calculate total / 用循环计算总和

# Simple Chinese explanation / 简单中文解释
# loop 可以重复执行代码。for loop 常用来处理列表里的每一个元素。

# Short English summary
# A loop repeats code and helps process many values.

# Beginner-friendly code example / 入门代码例子
for number in range(5):
    print("Range number:", number)

numbers = [10, 20, 30]

for number in numbers:
    print("List number:", number)

small_numbers = [1, 2, 3]

for number in small_numbers:
    print("Double:", number * 2)


def double_number(number):
    return number * 2


scores = [2, 4, 6]

for score in scores:
    print("Function result:", double_number(score))

prices = [1, 2, 3, 4]
total = 0

for price in prices:
    total = total + price

print("Total:", total)

# Common mistakes / 常见错误
# 1. Forgetting the colon after for.
# 2. Forgetting indentation inside the loop.
# 3. Changing the list in a confusing way while looping.

# Practice questions / 练习题
# 1. Print numbers from 0 to 9.
# 2. Create a list of names and print each name.
# 3. Use a loop to add all numbers in a list.
