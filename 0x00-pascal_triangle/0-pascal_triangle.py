#!/usr/bin/python3
"""a function def pascal_triangle(n): that returns 
   a list of lists of integers representing the Pascal's 
   triangle of n"""


def pascal_triangle(n):
    """Returns the pascal's triangle of n"""
    triangle = []

    if n <= 0:
        return triangle
    else: 
        triangle.append([1])
    
    for i in range(1, n):
        level = [1]
        lst = triangle[-1]
        length = len(lst)
        for idx in range(length):
            if idx < length - 1:
                level.append(lst[idx] + lst[idx + 1])
        level.append(1)
        triangle.append(level)
    return triangle