# Day 16 - Simple Calculator Project / 简单计算器小项目

# What I learned / 我学到了什么
# - Review input and float conversion / 复习输入和浮点数转换
# - Use if, elif, and else / 使用 if、elif 和 else
# - Handle division by zero / 处理除以 0 的情况
# - Build a small calculator project / 完成一个简单计算器小项目

# Simple Chinese explanation / 简单中文解释
# 这个小项目可以让用户输入两个数字和一个运算符。
# 程序会根据运算符进行加、减、乘、除计算。
# 如果用户选择除法，还需要避免除以 0 的错误。

# Short English summary
# This project builds a simple calculator.
# It uses input(), float(), conditional statements, and basic error handling.

# Beginner-friendly code example / 入门代码例子

try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operator = input("Choose an operator (+, -, *, /): ")

    if operator == "+":
        result = first_number + second_number
        print("Result:", result)
    elif operator == "-":
        result = first_number - second_number
        print("Result:", result)
    elif operator == "*":
        result = first_number * second_number
        print("Result:", result)
    elif operator == "/":
        if second_number == 0:
            print("Cannot divide by zero.")
        else:
            result = first_number / second_number
            print("Result:", result)
    else:
        print("Invalid operator.")

except ValueError:
    print("Invalid input. Please enter numbers only.")

# Common mistakes / 常见错误
# 1. Forgetting to convert input with float().
# 2. Forgetting quotation marks around operators like "+".
# 3. Forgetting to handle division by zero.
# 4. Writing too many conditions without clear structure.
# 5. Forgetting indentation inside if, elif, else, or try blocks.

# Practice questions / 练习题
# 1. Add a power operator ** to the calculator.
# 2. Add a message that explains which operation was used.
# 3. Turn the calculator logic into a function.
# 4. Let the user calculate again without restarting the program.
# 5. Improve the error messages for invalid input.
