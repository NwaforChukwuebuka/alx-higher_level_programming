#!/usr/bin/python3
# 101-add_attribute.py
# Nwafor Chukwuebuka
"""Defines an attribute adder function that add attr to objects"""


def add_attribute(objec, attr, val):
    """ Function that adds a new attribute to an object if it’s possible
    Args:
        objec (any): The object to add an attribute to.
        attr (str): The name of the attribute to add to object.
        val (any): The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(objec, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objec, attr, val)
