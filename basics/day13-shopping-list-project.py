# Day 13 - Shopping List Project / 购物清单小项目

# What I learned / 我学到了什么
# - Review lists / 复习列表
# - Use append() to add items / 使用 append() 添加项目
# - Use a loop to print list items / 使用循环输出列表内容
# - Build a small beginner project / 完成一个入门小项目

# Simple Chinese explanation / 简单中文解释
# 这个小项目用 list 保存购物清单。
# 用户可以不断输入想买的东西，然后程序把它们加入列表。
# 最后程序会把完整的购物清单打印出来。

# Short English summary
# This project stores shopping items in a list.
# It uses input(), append(), while loop, and for loop.

# Beginner-friendly code example / 入门代码例子

shopping_list = []

print("Welcome to the Shopping List Project!")
print("Type 'done' when you finish adding items.")

while True:
    item = input("Enter an item: ")

    if item == "done":
        break

    shopping_list.append(item)
    print(item, "has been added.")

print("\nYour shopping list:")

for item in shopping_list:
    print("-", item)

print("Total items:", len(shopping_list))

# Common mistakes / 常见错误
# 1. Forgetting to create an empty list first.
# 2. Forgetting to use append() to add new items.
# 3. Forgetting to use break to stop the while loop.
# 4. Writing Done instead of done, because strings are case-sensitive.
# 5. Forgetting indentation inside if or while blocks.

# Practice questions / 练习题
# 1. Add a message when the shopping list is empty.
# 2. Allow the user to remove an item from the list.
# 3. Print item numbers before each shopping item.
# 4. Change done to q as the stop command.
# 5. Turn the shopping list logic into a function.
