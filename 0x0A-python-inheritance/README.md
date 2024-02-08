# Python Class Inheritance Project

## Introduction
This project delves into the concept of class inheritance in Python. Through practical exercises, I have learnt about superclass-subclass relationships, method overriding, and multiple inheritance. The project consists of various tasks aimed at solidifying my understanding of these concepts.

## Function Prototypes

### 0. Lookup
**File:** `0-lookup.py`

```python
def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
```

### 1. My List
**File:** `1-my_list.py`

```python
class MyList(list):
    """Python class MyList that inherits from list."""
    
    def print_sorted(self):
        """Public instance method that prints the list in ascending sorted order."""
```

### 2. Exact Same Object
**File:** `2-is_same_class.py`

```python
def is_same_class(obj, a_class):
    """Returns True if an object is exactly an instance of a specified class; otherwise False."""
```

### 3. Same Class or Inherit From
**File:** `3-is_kind_of_class.py`

```python
def is_kind_of_class(obj, a_class):
    """Returns True if an object is an instance or inherited instance of a specified class; otherwise False."""
```

### 4. Only Subclass Of
**File:** `4-inherits_from.py`

```python
def inherits_from(obj, a_class):
    """Returns True if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise False."""
```

### 5. Geometry Module
**File:** `5-base_geometry.py`

```python
class BaseGeometry:
    """An empty Python class BaseGeometry."""
```

### 6. Improve Geometry
**File:** `6-base_geometry.py`

```python
class BaseGeometry:
    """Python class BaseGeometry."""
    
    def area(self):
        """Public instance method that raises an Exception with the message 'area() is not implemented'."""
```

### 7. Integer Validator
**File:** `7-base_geometry.py`

```python
class BaseGeometry:
    """Python class BaseGeometry."""
    
    def integer_validator(self, name, value):
        """Public instance method that validates the parameter value."""
```

### 8. Rectangle
**File:** `8-rectangle.py`

```python
class Rectangle(BaseGeometry):
    """Python class Rectangle that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Instantiation with width and height."""
```

### 9. Full Rectangle
**File:** `9-rectangle.py`

```python
class Rectangle(BaseGeometry):
    """Python class Rectangle that inherits from BaseGeometry."""
    
    def area(self):
        """Implementation of the method area()."""
    
    def __str__(self):
        """Special method to print Rectangles in the format [Rectangle] <width>/<height>."""
```

### 10. Square #1
**File:** `10-square.py`

```python
class Square(Rectangle):
    """Python class Square that inherits from Rectangle."""
    
    def __init__(self, size):
        """Instantiation with size."""
    
    def area(self):
        """Implementation of the area() method."""
```

### 11. Square #2
**File:** `11-square.py`

```python
class Square(Rectangle):
    """Python class Square that inherits from Rectangle."""
    
    def __str__(self):
        """Special method to print squares in the format [Square] <width>/<height>."""
```

### 12. My Integer
**File:** `100-my_int.py`

```python
class MyInt(int):
    """Python class MyInt that inherits from int."""
    
    # Inversion of the == and != operators
```

### 13. Can I?
**File:** `101-add_attribute.py`

```python
def add_attribute(obj, att, value):
    """Python function that adds a new attribute to an object if possible."""
```
