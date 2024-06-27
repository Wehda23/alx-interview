#!/usr/bin/python3
"""
0-pascale_triangle
"""


def pascal_triangle(n):
    """
    Representing pascale triangle of n
    Returns a list of list of integers
    Returns empty list if n <= 0
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle