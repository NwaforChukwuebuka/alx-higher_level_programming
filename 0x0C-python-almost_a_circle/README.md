Python - Almost a circle
------------------------

### Base Class:

#### Attributes:
- `__nb_objects`: Private class attribute tracking the number of objects created.
- `id`: Public instance attribute representing the object's identifier.

#### Methods:

1. **Constructor:**
   - `__init__(self, id=None)`: Initializes the object with a unique identifier. If `id` is not provided, it increments `__nb_objects`.

2. **Serialization:**
   - `to_json_string(list_dictionaries)`: Static method returning the JSON string serialization of a list of dictionaries.

3. **File I/O:**
   - `save_to_file(cls, list_objs)`: Class method writing the JSON serialization of a list of objects to a file.
   - `from_json_string(json_string)`: Static method returning a list of objects deserialized from a JSON string.
   - `load_from_file(cls)`: Class method returning a list of objects instantiated from a JSON file.
   - `save_to_file_csv(cls, list_objs)`: Class method writing the CSV serialization of a list of objects to a file.
   - `load_from_file_csv(cls)`: Class method returning a list of objects instantiated from a CSV file.

4. **Object Instantiation:**
   - `create(cls, **dictionary)`: Class method instantiating an object with provided attributes.

5. **Drawing:**
   - `draw(list_rectangles, list_squares)`: Static method that draws Rectangle and Square instances in a GUI window using the turtle module.

### Rectangle Class (Inherits from Base):

#### Attributes:
- `__width`, `__height`, `__x`, `__y`: Private instance attributes with getter/setter methods.

#### Methods:

1. **Constructor:**
   - `__init__(self, width, height, x=0, y=0, id=None)`: Initializes the rectangle with width, height, and position.

2. **Geometry:**
   - `area(self)`: Public method returning the area of the Rectangle instance.

3. **Display and String Representation:**
   - `display(self)`: Public method printing the Rectangle instance to stdout using the # character.
   - `__str__(self)`: Overridden method to print a Rectangle instance in the format [Rectangle] (<id>) <x>/<y>.

4. **Update and Dictionary Representation:**
   - `update(self, *args, **kwargs)`: Public method updating an instance of a Rectangle with given attributes.
   - `to_dictionary(self)`: Public method returning the dictionary representation of a Rectangle instance.

### Square Class (Inherits from Rectangle):

#### Methods:

1. **Constructor:**
   - `__init__(self, size, x=0, y=0, id=None)`: Initializes the square with size and position.

2. **String Representation:**
   - `__str__(self)`: Overridden method to print a Square instance in the format [Square] (<id>) <x>/<y>.

3. **Update and Dictionary Representation:**
   - `update(self, *args, **kwargs)`: Public method updating an instance of a Square with given attributes.
   - `to_dictionary(self)`: Public method returning the dictionary representation of a Square instance.
