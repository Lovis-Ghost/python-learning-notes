# Day 2 - Python Lists / Python 列表

# What I learned / 我学到了什么
# - Create a list / 创建列表
# - Add data to a list / 向列表添加数据
# - Get data by index / 用索引取得数据
# - Check list length / 查看列表长度

# Simple Chinese explanation / 简单中文解释
# list 可以保存多个数据。索引从 0 开始，所以第一个元素是 numbers[0]。

# Short English summary
# A list stores many values in one variable.

# Beginner-friendly code example / 入门代码例子
numbers = [1, 2, 3, 4, 5]

print("Original list:", numbers)

numbers.append(6)

print("After adding 6:", numbers)
print("First element:", numbers[0])
print("Length of list:", len(numbers))

fruits = ["apple", "banana", "orange"]
print("My fruits:", fruits)

# Common mistakes / 常见错误
# 1. The first index is 0, not 1.
# 2. Forgetting square brackets: numbers = 1, 2, 3
# 3. Using an index that does not exist, like numbers[10].

# Practice questions / 练习题
# 1. Create a list of three favorite foods.
# 2. Add one more food to the list.
# 3. Print the second item in the list.
