#!/usr/bin/python3
"""
This module contains implementation for the 2D
Matrix populart interview question
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place."""
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    matrix_len = len(matrix)

    for i in range(matrix_len):
        for j in range(i, matrix_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for array in matrix:
        array.reverse()

    return matrix
