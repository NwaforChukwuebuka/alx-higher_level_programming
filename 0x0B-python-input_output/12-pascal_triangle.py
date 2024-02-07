#!/usr/bin/python3
# 12-pascal_triangle.py
# Nwafor Chukwuebuka
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n
     Returns a list of numbers in pascals triangle.
    """
    if n <= 0:
        return []

    pas_tri = [[1]]
    while len(pas_tri) != n:
        tri = pas_tri[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        pas_tri.append(tmp)
    return pas_tri
