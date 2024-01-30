## Project: More Classes and Objects in Python

This project focuses on object-oriented programming in Python, covering topics such as class methods, static methods, class vs instance attributes, and special methods like `__str__` and `__repr__`.

### File Structure:

- `0-rectangle.py`: Defines an empty Python class for a rectangle.
- `1-rectangle.py`: Defines a rectangle class with private instance attributes for width and height, along with getters and setters.
- `2-rectangle.py`: Adds methods to calculate the area and perimeter of the rectangle.
- `3-rectangle.py`: Implements the `__str__` method to print the rectangle with `#` characters.
- `4-rectangle.py`: Implements the `__repr__` method to return a string representation of the rectangle.
- `5-rectangle.py`: Adds a `__del__` method to print a message when a rectangle instance is deleted.
- `6-rectangle.py`: Introduces a class attribute `number_of_instances` to track the number of instances created.
- `7-rectangle.py`: Adds a class attribute `class_symbol` to customize the string representation symbol.
- `8-rectangle.py`: Includes a static method to compare two rectangles and return the one with the greater area.
- `9-rectangle.py`: Implements a class method to create a square with equal width and height.
- `101-nqueens.py`: Solves the N queens puzzle, placing non-attacking queens on an NxN chessboard.

### Usage:

- For each file, the provided class or functions can be imported and used as needed in other Python scripts.
- The `101-nqueens.py` script can be executed from the command line to solve the N queens puzzle for a given board size.

### Notes:

- Each file builds upon the previous one, adding new functionality or improvements to the Rectangle class.
- Proper error handling and documentation are maintained throughout the project.
- The code follows PEP 8 style guidelines and is well-commented for clarity.
- Test files in the `tests` folder can be used to verify the correctness of each class and method.
