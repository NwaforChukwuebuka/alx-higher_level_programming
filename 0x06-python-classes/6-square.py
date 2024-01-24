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

    def __init__(self, size=0, position=(0, 0)) -> None:
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
        self.__position = position

    @property
    def size(self):
        """setter for size"""
        return self.__size

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @size.setter
    def size(self, size):
        """setter for size"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, value):
        """setter for position"""
        flag = 0

        while 1:
            if type(value) is not tuple or len(value) != 2:
                flag += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                flag += 1
                break
            if value[0] < 0 or value[1] < 0:
                flag += 1
                break
        if flag == 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        """prints square of # based on given size """

        if(self.__size == 0):
            print("")

        else:
            for y in range(self.__position[1]):
                print()
            for col in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
