# Day 7 - Python Strings / Python 字符串

# What I learned / 我学到了什么
# - Create a string / 创建字符串
# - Print a string / 输出字符串
# - Get one character by index / 用索引取得一个字符
# - Check string length with len() / 用 len() 查看字符串长度
# - Use simple string methods / 使用简单的字符串方法
# - Join strings together / 连接字符串

# Simple Chinese explanation / 简单中文解释
# string 是字符串，用来保存文字内容。
# 字符串需要放在引号里面，例如 "Hello"。
# 字符串的索引从 0 开始，所以第一个字符是 text[0]。
# len() 可以计算字符串有多少个字符。
# upper(), lower(), strip() 是常用的字符串方法。

# Short English summary
# A string stores text. Python can print strings, get characters by index,
# check length, change letter case, remove spaces, and join strings together.

# Beginner-friendly code examples / 入门代码例子

# 1. Creating a string / 创建字符串
message = "Hello Python"
name = "Lovis"

# 2. Printing a string / 输出字符串
print(message)
print(name)

# 3. String index / 字符串索引
word = "Python"

print("First character:", word[0])
print("Second character:", word[1])
print("Last character:", word[-1])

# 4. String length using len() / 使用 len() 查看字符串长度
print("Length of word:", len(word))

# 5. String methods / 字符串方法
text = "  Python Is Fun  "

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Remove spaces:", text.strip())

# 6. Simple string concatenation / 简单字符串连接
first_name = "Lovis"
last_name = "Ghost"

full_name = first_name + " " + last_name

print("Full name:", full_name)

greeting = "Hello, " + name + "!"

print(greeting)

# Common mistakes / 常见错误
# 1. Forgetting quotation marks: name = Lovis
# 2. Using an index that does not exist, like word[10].
# 3. Forgetting that the first index is 0, not 1.
# 4. Trying to add a string and a number directly: "Age: " + 18
# 5. Forgetting brackets when using a method: text.upper

# Practice questions / 练习题
# 1. Create a string variable called city and print it.
# 2. Print the first character of your name.
# 3. Use len() to check the length of your favorite word.
# 4. Create a string with extra spaces and use strip().
# 5. Join your first name and last name into one full name.
