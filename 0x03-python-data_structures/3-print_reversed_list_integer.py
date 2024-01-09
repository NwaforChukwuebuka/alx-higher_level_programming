#!/usr/bin/python3

def print_reversed_list_integer(my_list=None):
    """Print all integers of a list in reverse order."""
    if my_list is None:
        my_list = []
    if not isinstance(my_list, list):
        return

    reversed_list = list(my_list)
    reversed_list.reverse()
    for i in reversed_list:
        print("{:d}".format(i))
