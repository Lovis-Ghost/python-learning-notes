# Day 12 - Score Checker Project / 成绩判断小项目

# What I learned / 我学到了什么
# - Review input and type conversion / 复习输入和类型转换
# - Use if, elif, and else / 使用 if、elif 和 else
# - Write a small beginner project / 编写一个入门小项目
# - Check user input with simple conditions / 用简单条件判断用户输入

# Simple Chinese explanation / 简单中文解释
# 这个小项目可以根据用户输入的分数判断等级。
# input() 得到的是字符串，所以需要用 int() 转换成整数。
# if, elif, else 可以根据不同分数输出不同结果。

# Short English summary
# This small project checks a score and prints a grade.
# It uses input(), int(), and conditional statements.

# Beginner-friendly code example / 入门代码例子

score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

# Extra practice example / 额外练习例子

if score >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")

# Common mistakes / 常见错误
# 1. Forgetting to convert input with int().
# 2. Writing conditions in the wrong order.
# 3. Forgetting the colon after if, elif, or else.
# 4. Forgetting indentation inside the condition block.
# 5. Using = instead of == when comparing values.

# Practice questions / 练习题
# 1. Change the grade rules and test different scores.
# 2. Add a message for excellent students when score is greater than or equal to 95.
# 3. Add a check for invalid scores below 0 or above 100.
# 4. Ask the user to enter three scores and calculate the average.
# 5. Turn the score checker into a function.
