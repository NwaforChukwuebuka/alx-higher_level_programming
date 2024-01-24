#!/usr/bin/python3
""""
A Square class with private instance attr 'size'
               and  public instance 'area()'.

"""


class Square:
    """ A Square class with private instance attr 'size'
                        and  public instance 'area()'

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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def my_print(self):

        x = 0
        if(self.__size == 0):
            print("")

        else:
            while(x < self.__size):
                for i in range(1, self.__size+1):
                    print("#", end="")
                x += 1
                print()
