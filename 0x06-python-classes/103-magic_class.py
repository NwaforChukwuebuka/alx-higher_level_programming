import math
""" Magic Circle class"


class MagicClass:
    """Magic circle Class with given radius for area and circum calcs."""

    def __init__(self, radius=0):
        """
        Initialize the MagicClass instance with a specified radius.

        Args:
            radius (int or float, optional): The radius of the magic circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calc the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calc the circum of  circle.

        Returns:
            float: The circum of the circle.
        """
        return 2 * math.pi * self.__radius
