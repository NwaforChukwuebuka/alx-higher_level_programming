#!/usr/bin/python3
# 1-rectangle.py
# Nwafor Chukwuebuka
"""Defines a Rectangle class."""


class Rectangle:
    """Creates a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    """ width property """

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Height property """
    @property
    def height(self):
        """Getter for  the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height of the Rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the Area of the reactangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return(0)
        return (2 * (self.__height + self.__width))
