#!/usr/bin/python3
# 8-rectangle.py
# Nwafor Chukwuebuka
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle from BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle object.

        Args:
            width (int): The new Rectangle’s with.
            height (int): The new Rectangle’s height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
