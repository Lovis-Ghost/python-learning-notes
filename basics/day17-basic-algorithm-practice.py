# Day 17 - Basic Algorithm Practice / 基础算法练习

# What I learned / 我学到了什么
# - Understand what an algorithm means / 理解什么是算法
# - Use loops to solve simple problems / 使用循环解决简单问题
# - Find the maximum number in a list / 找出列表中的最大值
# - Count values with a dictionary / 使用字典计数
# - Practice step-by-step thinking / 练习一步一步思考

# Simple Chinese explanation / 简单中文解释
# algorithm 可以理解为解决问题的步骤。
# 对初学者来说，算法不一定很复杂。
# 先学会用循环、列表、字典解决简单问题，是刷 LeetCode 前的重要基础。

# Short English summary
# An algorithm is a step-by-step way to solve a problem.
# Beginner algorithm practice often uses loops, lists, and dictionaries.

# Beginner-friendly code examples / 入门代码例子

# 1. Find the maximum number / 找出最大值
numbers = [3, 8, 2, 10, 5]

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print("Max number:", max_number)

# 2. Count even numbers / 统计偶数数量
numbers = [1, 2, 3, 4, 5, 6]

even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count = even_count + 1

print("Even count:", even_count)

# 3. Count characters with a dictionary / 使用字典统计字符
word = "banana"
char_count = {}

for char in word:
    if char not in char_count:
        char_count[char] = 0
    char_count[char] = char_count[char] + 1

print("Character count:", char_count)

# 4. Find a target number / 查找目标数字
numbers = [4, 7, 9, 12, 15]
target = 12
found = False

for number in numbers:
    if number == target:
        found = True
        break

print("Found target:", found)

# Common mistakes / 常见错误
# 1. Trying to memorize code without understanding the steps.
# 2. Forgetting to initialize variables before the loop.
# 3. Using the wrong condition inside if.
# 4. Forgetting to update the answer inside the loop.
# 5. Not testing the code with different examples.

# Practice questions / 练习题
# 1. Find the smallest number in a list.
# 2. Count how many numbers are greater than 10.
# 3. Count each letter in your own name.
# 4. Check whether a list contains a target number.
# 5. Write the Chinese idea first, then convert it into Python code.
