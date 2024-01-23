#!/usr/bin/python3
""""
A Square class with private instance attr 'size'.

"""


class Square:
    """ A Square class with private instance attr 'size'.

    Attributes:
        size (int) : The size of the instance. Default is zero

    Raises:
        TypeError: if the size is not an integer
        ValueError: if the size is less than 0

    Example:
        >>> obj = MyClass(size=5)
        >>> print(obj.size)
        5

    """

    def __init__(self, size=0) -> None:
        """
        Initialize the instance with a specified size.

        Args:
            size (int, optional): The size of the instance. Defaults to 0.
                Must be an integer, and size >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
