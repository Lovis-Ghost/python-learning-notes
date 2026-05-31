# Day 9 - Nested Loops / 嵌套循环

# What I learned / 我学到了什么
# - Use a loop inside another loop / 在一个循环里面使用另一个循环
# - Understand outer loop and inner loop / 理解外层循环和内层循环
# - Print simple patterns / 输出简单图案
# - Read data from nested lists / 读取嵌套列表中的数据

# Simple Chinese explanation / 简单中文解释
# nested loop 是嵌套循环，意思是一个循环里面还有另一个循环。
# 外层循环通常控制行数，内层循环通常控制每一行里面的内容。
# 嵌套循环常用于打印图案、处理表格和读取二维列表。

# Short English summary
# A nested loop means one loop inside another loop.
# It is useful for patterns, tables, and nested lists.

# Beginner-friendly code examples / 入门代码例子

# 1. Basic nested loop / 基础嵌套循环
for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)

# 2. Print a simple square pattern / 输出简单正方形图案
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()

# 3. Print a triangle pattern / 输出三角形图案
for row in range(1, 5):
    for col in range(row):
        print("*", end=" ")
    print()

# 4. Nested list / 嵌套列表
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for number in row:
        print(number)

# 5. Calculate total from nested list / 计算嵌套列表中的总和
total = 0

for row in matrix:
    for number in row:
        total = total + number

print("Total:", total)

# Common mistakes / 常见错误
# 1. Forgetting indentation in the inner loop.
# 2. Confusing the outer loop variable and inner loop variable.
# 3. Forgetting print() after each row when printing a pattern.
# 4. Making the nested loop too complicated too early.

# Practice questions / 练习题
# 1. Use nested loops to print a 4 by 4 square of stars.
# 2. Use nested loops to print numbers from a nested list.
# 3. Create a 2 by 3 nested list and print each value.
# 4. Calculate the total of all numbers in a nested list.
# 5. Print a triangle pattern with 5 rows.
