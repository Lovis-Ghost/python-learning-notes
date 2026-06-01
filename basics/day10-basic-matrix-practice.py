# Day 10 - Basic Matrix Practice / 基础矩阵练习

# What I learned / 我学到了什么
# - Understand a matrix as a nested list / 把矩阵理解成嵌套列表
# - Read rows and columns / 读取行和列
# - Use nested loops with a matrix / 用嵌套循环处理矩阵
# - Calculate the total of matrix values / 计算矩阵中所有数字的总和

# Simple Chinese explanation / 简单中文解释
# matrix 可以理解为一个二维表格。
# 在 Python 里，可以用 nested list 来表示 matrix。
# 外层 list 表示行，内层 list 表示每一行里的数字。

# Short English summary
# A matrix can be represented by a nested list in Python.
# Each inner list is one row of the matrix.

# Beginner-friendly code examples / 入门代码例子

# 1. Create a simple matrix / 创建一个简单矩阵
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:", matrix)

# 2. Print one row / 输出一行
print("First row:", matrix[0])
print("Second row:", matrix[1])

# 3. Print one value / 输出一个具体的值
print("First value:", matrix[0][0])
print("Middle value:", matrix[1][1])

# 4. Print all rows / 输出所有行
for row in matrix:
    print(row)

# 5. Print all values / 输出所有数字
for row in matrix:
    for number in row:
        print(number)

# 6. Calculate total / 计算总和
total = 0

for row in matrix:
    for number in row:
        total = total + number

print("Total:", total)

# 7. Count rows and columns / 计算行数和列数
row_count = len(matrix)
column_count = len(matrix[0])

print("Rows:", row_count)
print("Columns:", column_count)

# Common mistakes / 常见错误
# 1. Forgetting that matrix[0] means the first row.
# 2. Confusing matrix[0][1] with matrix[1][0].
# 3. Forgetting that list index starts from 0.
# 4. Assuming every row has the same length without checking.

# Practice questions / 练习题
# 1. Create a 2 by 3 matrix and print it.
# 2. Print the first row of your matrix.
# 3. Print one specific value using two indexes.
# 4. Use nested loops to print all numbers.
# 5. Calculate the total of all numbers in your matrix.
