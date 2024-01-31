0x07 Python Test-Driven Development
This repository contains solutions to the Python Test-Driven Development project of ALX Software Engineering program.

Tasks Overview
0. Integers Addition
Write a function that adds two integers. The function prototype is:

python
Copy code
def add_integer(a, b=98):
    """
    Function to add two integers.

    Args:
        a (int): First integer.
        b (int, optional): Second integer. Defaults to 98.

    Returns:
        int: Sum of a and b.

    Raises:
        TypeError: If a or b is not an integer.
    """
    # Function implementation
1. Divide a Matrix
Write a function that divides all elements of a matrix by a given number. The function prototype is:

python
Copy code
def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix.

    Args:
        matrix (list): List of lists containing integers or floats.
        div (int/float): Number to divide the matrix elements by.

    Returns:
        list: New matrix with elements divided by div.

    Raises:
        TypeError: If matrix contains non-numeric elements or div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Function implementation
2. Say My Name
Write a function that prints a given first name and last name. The function prototype is:

python
Copy code
def say_my_name(first_name, last_name=""):
    """
    Function to print a name.

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Function implementation
3. Print Square
Write a function that prints a square with the character '#'. The function prototype is:

python
Copy code
def print_square(size):
    """
    Function to print a square.

    Args:
        size (int): Size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    # Function implementation
4. Text Indentation
Write a function that prints a text with two new lines after each '.', '?' and ':'. The function prototype is:

python
Copy code
def text_indentation(text):
    """
    Function to print text with indentation.

    Args:
        text (str): Input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Function implementation
5. Max Integer - Unittest
Write unittests for the function max_integer(list=[]) using the unittest module.

How to Run
To run each task, execute the corresponding Python script. For example, to run the first task:

bash
Copy code
./0-add_integer.py
To run the tests for each task, use the following command:

bash
Copy code
python3 -m doctest -v ./tests/<filename>.txt
Author
Created by Nwafor Chukwuebuka
