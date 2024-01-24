#!/usr/bin/python3
"""Class Square with private instance attri size and position
public instance methods to calculate area and print square
"""


class Square:
    """Class with private instance attributes size and position
     """

    def __init__(self, size=0, position=(0, 0)):
        """Instantiates attribute position to (0, 0) and size = 0"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the private instance attribute size"""
        return(self.__size)

    @property
    def position(self):
        """gets the private instance attribute position"""
        return(self.__position)

    @size.setter
    def size(self, value):
        """sets the private instance attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """sets the private instance attribute position"""
        flag = 0
        while 1:
            if type(value) is not tuple or len(value) != 2:
                flag += 1
                break
            if type(value[1]) is not int or type(value[0]) is not int:
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
        """calcs and returns square area"""
        return(self.__size * self.__size)

    def my_print(self):
        """prints square of size # num of times"""
        if self.__size > 0:
            for n in range(self.__position[1]):
                print()
            for col in range(self.__size):
                for m in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def my_print_string(self):
        """format my_print"""
        sq_str = ""
        if self.__size > 0:
            for n in range(self.__position[1]):
                sq_str = sq_str + "\n"
            for row in range(self.__size):
                for m in range(self.__position[0]):
                    sq_str = sq_str + " "
                for col in range(self.__size):
                    sq_str = sq_str + "#"
                if row is not (self.__size - 1):
                    sq_str = sq_str + "\n"
        return sq_str

    def __repr__(self):
        """returns square rep as a string"""
        return (self.my_print_string())
