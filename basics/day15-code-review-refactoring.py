# Day 15 - Code Review and Refactoring / 代码检查和重构

# What I learned / 我学到了什么
# - Understand code review / 理解代码检查
# - Understand refactoring / 理解代码重构
# - Improve variable names / 优化变量命名
# - Reduce repeated code / 减少重复代码
# - Make code easier to read / 让代码更容易阅读

# Simple Chinese explanation / 简单中文解释
# code review 是检查代码，看看代码是否清楚、是否有错误、是否容易理解。
# refactoring 是在不改变功能的情况下，让代码变得更整洁。
# 对初学者来说，清楚的变量名、正确的缩进、少重复代码非常重要。

# Short English summary
# Code review means checking code quality.
# Refactoring means improving code structure without changing the result.

# Beginner-friendly code examples / 入门代码例子

# 1. Before refactoring / 重构前
s = 85

if s >= 60:
    print("Pass")
else:
    print("Fail")

# 2. After refactoring: clear variable name / 重构后：使用清楚的变量名
score = 85

if score >= 60:
    print("Pass")
else:
    print("Fail")

# 3. Before refactoring: repeated code / 重构前：重复代码
print("Student: Alice")
print("Score: 90")
print("Student: Bob")
print("Score: 80")

# 4. After refactoring: use a list and loop / 重构后：使用列表和循环
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 80}
]

for student in students:
    print("Student:", student["name"])
    print("Score:", student["score"])

# 5. Refactor score checking into a function / 把成绩判断重构成函数
def check_result(score):
    if score >= 60:
        return "Pass"
    return "Fail"

print(check_result(75))
print(check_result(50))

# Common mistakes / 常见错误
# 1. Changing the program result while refactoring.
# 2. Using unclear variable names like a, b, x, y too often.
# 3. Making one function too long.
# 4. Repeating the same code many times.
# 5. Refactoring too early before understanding the code.

# Practice questions / 练习题
# 1. Rename unclear variables in an old practice file.
# 2. Find repeated code and use a loop to improve it.
# 3. Turn a simple score checker into a function.
# 4. Add comments to explain important code.
# 5. Review one old file and write down three improvements.
