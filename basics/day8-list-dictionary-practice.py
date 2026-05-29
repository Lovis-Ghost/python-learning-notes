# Day 8 - List and Dictionary Practice / 列表和字典综合练习

# What I learned / 我学到了什么
# - Review lists / 复习列表
# - Review dictionaries / 复习字典
# - Combine a list with dictionaries / 把列表和字典结合起来
# - Use a loop to read several records / 使用循环读取多条记录

# Simple Chinese explanation / 简单中文解释
# list 可以保存多个数据。
# dictionary 可以用 key-value 的方式保存一组信息。
# 一个 dictionary 可以表示一个学生，多名学生可以放在一个 list 里面。

# Short English summary
# Lists store multiple items. Dictionaries store related information.
# A list of dictionaries can be used to store several records.

# Beginner-friendly code examples / 入门代码例子

scores = [80, 90, 75, 88]

print("Scores:", scores)
print("First score:", scores[0])
print("Number of scores:", len(scores))

scores.append(95)
print("Updated scores:", scores)

student = {
    "name": "Lovis",
    "university": "UKM",
    "score": 90
}

print("Student name:", student["name"])
print("University:", student["university"])
print("Score:", student["score"])

student["score"] = 95
print("Updated student:", student)

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 78},
    {"name": "Chen", "score": 92}
]

for student in students:
    print(student["name"], student["score"])

high_score_names = []

for student in students:
    if student["score"] >= 80:
        high_score_names.append(student["name"])

print("High score students:", high_score_names)

# Common mistakes / 常见错误
# 1. List index starts from 0.
# 2. Dictionary keys need quotation marks.
# 3. Do not use a key that does not exist.
# 4. student["name"] and student[0] are different.

# Practice questions / 练习题
# 1. Create a list with five numbers and print the last number.
# 2. Create a dictionary with your name, university, and major.
# 3. Create a list of three dictionaries.
# 4. Use a loop to print each name.
# 5. Print only names with score greater than or equal to 80.
