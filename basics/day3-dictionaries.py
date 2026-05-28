# Day 3 - Python Dictionaries / Python 字典

# What I learned / 我学到了什么
# - Create a dictionary / 创建字典
# - Store key-value data / 保存键值对数据
# - Read and update values / 读取和更新数据

# Simple Chinese explanation / 简单中文解释
# dictionary 用 key 和 value 保存资料。例如 name 是 key，Lovis 是 value。

# Short English summary
# A dictionary stores information with keys and values.

# Beginner-friendly code example / 入门代码例子
student = {
    "name": "Lovis",
    "age": 24,
    "major": "Artificial Intelligence",
}

print("Student name:", student["name"])
print("Student age:", student["age"])

student["university"] = "UKM"

print("Updated dictionary:", student)

# Common mistakes / 常见错误
# 1. Forgetting quotation marks around string keys.
# 2. Using a key that does not exist.
# 3. Forgetting commas between dictionary items.

# Practice questions / 练习题
# 1. Create a dictionary for a book.
# 2. Add the book title, author, and year.
# 3. Print the book title.
