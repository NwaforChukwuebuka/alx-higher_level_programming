#!/usr/bin/python3

"""Define a class Square representing a square.

This module provides a simple Square class with methods to get and set the
size, calculate the area, and define various comparison operators (==, !=, <,
<=, >, >=) based on the area of two squares.
"""


class Square:
    """Represent a square with methods for size, area, and comparisons."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, obj2):
        """Define the == comparison to a Square."""
        return self.area() == obj2.area()

    def __ne__(self, obj2):
        """Define the != comparison to a Square."""
        return self.area() != obj2.area()

    def __lt__(self, obj2):
        """Define the < comparison to a Square."""
        return self.area() < obj2.area()

    def __le__(self, obj2):
        """Define the <= comparison to a Square."""
        return self.area() <= obj2.area()

    def __gt__(self, obj2):
        """Define the > comparison to a Square."""
        return self.area() > obj2.area()

    def __ge__(self, obj2):
        """Define the >= comparison to a Square."""
        return self.area() >= obj2.area()
