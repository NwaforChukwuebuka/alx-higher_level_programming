#!/usr/bin/python3
# 7-base_geometry.py
# Nwafor Chukwuebuka
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry empty class"""
    pass

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer parameter.

        Args:
            name: The parameter's name.
            value: The parameter's value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not positive.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
