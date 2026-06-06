"""
2D Matrix Traversal

Given a 2D matrix, traverse it in row-major order (left to right, top to bottom) and print every element. Then modify your solution to traverse it in column-major order.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Row-major output:    1 2 3 4 5 6 7 8 9
# Column-major output: 1 4 7 2 5 8 3 6 9
"""


def row_matrix_traversal(matrix):

    for row in matrix:
        for ele in row:
            print(ele, end="--")


def col_matrix_traversal(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
           ele = matrix[j][i]
           print(ele, end="--")
    


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("Row Major Traversal: ")
row_matrix_traversal(matrix)
print("\n")
print("Column Major Traversal: ")
col_matrix_traversal(matrix)