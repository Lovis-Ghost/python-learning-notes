# Day 14 - Error Handling / 错误处理

# What I learned / 我学到了什么
# - Understand common Python errors / 理解常见 Python 错误
# - Use try and except / 使用 try 和 except
# - Handle invalid user input / 处理无效用户输入
# - Make beginner projects more stable / 让入门小项目更稳定

# Simple Chinese explanation / 简单中文解释
# error handling 是错误处理。
# 当用户输入错误内容时，程序可能会报错并停止运行。
# try 和 except 可以帮助我们捕获错误，让程序继续运行或输出友好的提示。

# Short English summary
# Error handling helps a program deal with problems safely.
# try and except can catch errors and show friendly messages.

# Beginner-friendly code examples / 入门代码例子

# 1. Common error example / 常见错误例子
# int("abc") will cause a ValueError.

# 2. Handle invalid number input / 处理无效数字输入
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid number.")

# 3. Score checker with error handling / 带错误处理的成绩判断
try:
    score = int(input("Enter your score: "))

    if score < 0 or score > 100:
        print("Score should be between 0 and 100.")
    elif score >= 60:
        print("Result: Pass")
    else:
        print("Result: Fail")

except ValueError:
    print("Invalid input. Please enter a number.")

# 4. Simple division example / 简单除法例子
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Common mistakes / 常见错误
# 1. Forgetting to put risky code inside try.
# 2. Catching the wrong error type.
# 3. Writing too much code inside one try block.
# 4. Forgetting that int(input()) can cause ValueError.
# 5. Using error handling to hide problems instead of understanding them.

# Practice questions / 练习题
# 1. Ask the user to enter a number and handle invalid input.
# 2. Improve the Day 12 score checker with try and except.
# 3. Handle division by zero in a small calculator.
# 4. Write a program that keeps asking until the user enters a valid number.
# 5. Compare a program with error handling and without error handling.
