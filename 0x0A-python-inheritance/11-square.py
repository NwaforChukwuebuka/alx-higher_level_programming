#!/usr/bin/python3
# 11-square.py
# Nwafor Chukwuebuka
"""Defines a Square. A subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square class."""

    def __init__(self, size):
        """Initialize a new square object.

        Args:
            size (int): The new square’s size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
