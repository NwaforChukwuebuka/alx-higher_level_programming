#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """ squares value of all integers of a matrix."""
    return ([list(map(lambda x: x ** 2, row)) for row in matrix])
