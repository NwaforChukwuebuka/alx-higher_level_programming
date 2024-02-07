#!/usr/bin/python3
# 1-write_file.py
# Nwafor Chukwuebuka
"""Defines a text file content writing function."""


def write_file(filename="", text=""):
    """Write text to the UTF_8 filename.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
