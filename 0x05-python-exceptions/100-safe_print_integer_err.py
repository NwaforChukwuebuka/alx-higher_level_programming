#!/usr/bin/python3
#Nwafor Chukwuebuka <e.nwafor13@gmail.com>
# 100-safe_print_integer_err.py

import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Return:
        True if print succeeds
        False if print fails
    """
    try:
        print("{:d}".format(value))
        return (True)
    
    except (ValueError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False) 
