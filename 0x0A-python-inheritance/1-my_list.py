#!/usr/bin/python3
# 1-my_list.py
# Nwafor Chukwuebuka
"""Defines a subclass MyList inheriting from built-in list method"""


class MyList(list):
    """Sorting the built-in list class"""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
