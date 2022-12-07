#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    return [[item**2 for item in row] for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
