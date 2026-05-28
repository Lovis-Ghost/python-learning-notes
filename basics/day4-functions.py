# Day 4 - Python Functions / Python 函数

# What I learned / 我学到了什么
# - Define a function / 定义函数
# - Use parameters / 使用参数
# - Return a result / 返回结果

# Simple Chinese explanation / 简单中文解释
# function 可以重复使用一段代码。参数可以把不同的数据传进函数。

# Short English summary
# A function helps us organize code and reuse it.

# Beginner-friendly code example / 入门代码例子
def say_hello():
    print("Hello Python")


say_hello()


def greet(student_name):
    print("Hello", student_name)


greet("Alice")
greet("Bob")


def add_numbers(first_number, second_number):
    return first_number + second_number


result = add_numbers(5, 7)
print("Result:", result)

student = {
    "name": "Tom",
    "age": 21,
}


def show_student(student_data):
    print("Name:", student_data["name"])
    print("Age:", student_data["age"])


show_student(student)

# Common mistakes / 常见错误
# 1. Forgetting the colon after def.
# 2. Forgetting indentation inside the function.
# 3. Confusing print() and return.

# Practice questions / 练习题
# 1. Write a function that prints your name.
# 2. Write a function that adds two numbers.
# 3. Write a function that shows a student's major.
