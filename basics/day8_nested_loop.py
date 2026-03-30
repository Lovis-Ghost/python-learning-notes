# Day 8 - Nested Loop (嵌套循环)
# Author: Lovis

# ===============================
# 🔹 1. 基础嵌套循环
# ===============================
def basic_nested_loop():
    print("Basic Nested Loop:")
    for i in range(3):
        for j in range(3):
            print(i, j)
    print()


# ===============================
# 🔹 2. 打印正方形
# ===============================
def square(n):
    print("Square Pattern:")
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
    print()


# ===============================
# 🔹 3. 左三角
# ===============================
def left_triangle(n):
    print("Left Triangle:")
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
    print()


# ===============================
# 🔹 4. 右三角
# ===============================
def right_triangle(n):
    print("Right Triangle:")
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()
    print()


# ===============================
# 🔹 5. 倒三角（进阶）
# ===============================
def inverted_triangle(n):
    print("Inverted Triangle:")
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print()
    print()


# ===============================
# 🔹 6. 乘法表（重点🔥）
# ===============================
def multiplication_table():
    print("Multiplication Table:")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i*j}", end=" ")
        print()
    print()


# ===============================
# 🚀 主函数（程序入口）
# ===============================
def main():
    basic_nested_loop()
    square(3)
    left_triangle(4)
    right_triangle(4)
    inverted_triangle(4)
    multiplication_table()


# ===============================
# ▶️ 运行入口
# ===============================
if __name__ == "__main__":
    main()
