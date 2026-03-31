"""
Day 9 - Matrix (List of Lists)

Topics:
- 2D List (Matrix)
- Nested Loop Traversal
- Basic Matrix Operations

Author: Lovis
"""

# ===============================
# 🔹 1. 创建矩阵
# ===============================
def create_matrix():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


# ===============================
# 🔹 2. 遍历矩阵
# ===============================
def print_matrix(matrix):
    print("Matrix:")
    for i in range(len(matrix)):          # 行
        for j in range(len(matrix[i])):   # 列
            print(matrix[i][j], end=" ")
        print()
    print()


# ===============================
# 🔹 3. 求和
# ===============================
def sum_matrix(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total += matrix[i][j]
    print("Sum:", total)
    print()


# ===============================
# 🔹 4. 找最大值
# ===============================
def max_matrix(matrix):
    max_val = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
    print("Max:", max_val)
    print()


# ===============================
# 🔹 5. 主对角线
# ===============================
def diagonal(matrix):
    print("Diagonal:")
    for i in range(len(matrix)):
        print(matrix[i][i], end=" ")
    print("\n")


# ===============================
# 🔹 6. 每行反转（挑战🔥）
# ===============================
def reverse_rows(matrix):
    print("Reversed Rows:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1, -1, -1):
            print(matrix[i][j], end=" ")
        print()
    print()


# ===============================
# 🔹 7. 查找元素（简单搜索）
# ===============================
def search(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                print(f"Found {target} at position ({i}, {j})")
                return
    print(f"{target} not found")
    print()


# ===============================
# 🚀 主函数
# ===============================
def main():
    matrix = create_matrix()

    print_matrix(matrix)
    sum_matrix(matrix)
    max_matrix(matrix)
    diagonal(matrix)
    reverse_rows(matrix)
    search(matrix, 5)
    search(matrix, 10)


# ===============================
# ▶️ 程序入口
# ===============================
if __name__ == "__main__":
    main()
