# Day 11 - File Reading and Writing / 文件读取和写入

# What I learned / 我学到了什么
# - Write text to a file / 把文字写入文件
# - Read text from a file / 从文件读取文字
# - Use with open() safely / 使用 with open() 安全地打开文件
# - Understand read mode and write mode / 理解读取模式和写入模式

# Simple Chinese explanation / 简单中文解释
# file 是文件，可以用来保存程序产生的数据。
# Python 可以把文字写入文件，也可以从文件中读取内容。
# with open() 可以帮助我们自动关闭文件，比较安全。

# Short English summary
# Python can write data to a file and read data from a file.
# The with open() syntax is a safe and common way to work with files.

# Beginner-friendly code examples / 入门代码例子

# 1. Write text to a file / 写入文字到文件
with open("day11_notes.txt", "w") as file:
    file.write("Hello Python file!\n")
    file.write("I am learning file reading and writing.\n")

print("File writing finished.")

# 2. Read text from a file / 从文件读取文字
with open("day11_notes.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)

# 3. Write several lines / 写入多行内容
lines = [
    "Python is useful.\n",
    "Files can store information.\n",
    "Practice makes progress.\n"
]

with open("day11_lines.txt", "w") as file:
    file.writelines(lines)

print("Multiple lines written.")

# 4. Read line by line / 一行一行读取
with open("day11_lines.txt", "r") as file:
    for line in file:
        print(line.strip())

# Common mistakes / 常见错误
# 1. Using r mode before the file exists.
# 2. Forgetting quotation marks around the file name.
# 3. Forgetting that w mode will overwrite old content.
# 4. Forgetting to add \n when writing multiple lines.
# 5. Not using with open(), so the file may not close properly.

# Practice questions / 练习题
# 1. Create a text file and write your name into it.
# 2. Write three lines about your Python learning progress.
# 3. Read the file content and print it.
# 4. Read a file line by line using a for loop.
# 5. Try changing w mode to a mode and observe the difference.
