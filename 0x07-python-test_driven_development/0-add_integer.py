#!/usr/bin/python3
# 0-add_integer.py
# Nwafor Chukwuebuka
"""Function for adding two integers"""


def add_integer(a, b=98):
    """Return the sum of two integers.

    Arguments:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b after typecasting them to integers.

    Raises:
    TypeError: If either a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
