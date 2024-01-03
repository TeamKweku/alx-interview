#!/usr/bin/python3
"""
This module contains the pascal triangle function
"""
def pascal_triangle(n):
    """
    Function that creates a pascal triangle based on the
    length provided
    """
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0) or (j == i):
                row.append(1)
            else:
                row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
        triangle.append(row)
    return triangle
