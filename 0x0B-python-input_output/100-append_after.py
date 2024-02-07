#!/usr/bin/python3
# 100-append_after.py
# Nwafor Chukwuebuka
"""Defines a text file insertion function at a specified position."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts string after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as book:
        for line in book:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
