#!/usr/bin/python3
# 4-append_write.py
# Nwafor Chukwuebuka
"""Defines a text file appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The str to append to the file.
    Returns:
        The num of char appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
