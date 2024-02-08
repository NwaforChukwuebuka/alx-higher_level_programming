#!/usr/bin/python3
# 2-is_same_class.py
# Nwafor Chukwuebuka
"""Defines a function that checks if obj is an instance of a class"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of the class 'a_class'
    Args:
        obj (any): The object we are checking
        a_class (any): The given class
    Returns:
        Bool: True if true and False if otherwise
    """

    if type(obj) == a_class:
        return True
    return False
