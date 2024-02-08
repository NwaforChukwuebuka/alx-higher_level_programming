#!/usr/bin/python3
# 3-is_kind_of_class.py
# Nwafor Chukwubuka
"""Defines a class and superclass checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
        
    Returns:
        True if obj is an instance or inherited instance of a_class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
