#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): Given list
        x (int): Total integer to print from list

    Returns:
        The number of integers printed.
    """
    int_printed = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            int_printed += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (int_printed)
