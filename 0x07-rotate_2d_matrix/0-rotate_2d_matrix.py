#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise.

    Args:
    matrix (list[list[int]]): The input n x n matrix to be rotated.

    Returns:
    None. The matrix is modified in place.
    """
    n = len(matrix)

    new_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_matrix[j][n - i - 1] = matrix[i][j]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = new_matrix[i][j]
