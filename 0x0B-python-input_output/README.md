---

## Python Input/Output

This project focuses on practicing file handling in Python. It utilizes built-in functions such as `with`, `open`, and `read`, along with the `json` module for reading and writing files, as well as serializing and deserializing objects with JSON.

### Tests ✔️

Folder containing test files provided by Holberton School.

### Function Prototypes 💾

Prototypes for functions written in this project:

| File                | Prototype                               |
|---------------------|-----------------------------------------|
| 0-read_file.py      | `def read_file(filename=""):`           |
| 1-number_of_lines.py| `def number_of_lines(filename=""):`     |
| 2-read_lines.py     | `def read_lines(filename="", nb_lines=0):` |
| 3-write_file.py     | `def write_file(filename="", text=""):` |
| 4-append_write.py   | `def append_write(filename="", text=""):`|
| 5-to_json_string.py| `def to_json_string(my_obj):`           |
| 6-from_json_string.py| `def from_json_string(my_str):`        |
| 7-save_to_json_file.py| `def save_to_json_file(my_obj, filename):` |
| 8-load_from_json_file.py| `def load_from_json_file(filename):` |
| 10-class_to_json.py | `def class_to_json(obj):`               |
| 14-pascal_triangle.py| `def pascal_triangle(n):`             |
| 100-append_after.py| `def append_after(filename="", search_string="", new_string=""):` |

### Tasks 📃

1. **Read file** (0-read_file.py):
   - Python function that prints the contents of a UTF8 text file to standard output.

2. **Number of lines** (1-number_of_lines.py):
   - Python function that returns the number of lines contained in a text file.

3. **Read n lines** (2-read_lines.py):
   - Python function that prints n lines of a UTF8 text file to standard output.

4. **Write to a file** (3-write_file.py):
   - Python function that writes a string to a UTF8 text file and returns the number of characters written.

5. **Append to a file** (4-append_write.py):
   - Python function that appends a string to the end of a UTF8 text file and returns the number of characters appended.

6. **To JSON string** (5-to_json_string.py):
   - Python function that returns the JSON string representation of an object.

7. **From JSON string to Object** (6-from_json_string.py):
   - Python function that returns the Python object represented by a JSON string.

8. **Save Object to a file** (7-save_to_json_file.py):
   - Python function that writes an object to a text file using JSON representation.

9. **Create object from a JSON file** (8-load_from_json_file.py):
   - Python function that creates an object from a .json file.

10. **Class to JSON** (10-class_to_json.py):
    - Python function that returns the dictionary description for simple Python data structures (lists, dictionaries, strings, integers, and booleans).

11. **Student to JSON** (11-student.py):
    - Python class Student that defines a student with public instance attributes `first_name`, `last_name`, and `age`, and a public method `to_json()`.

12. **Student to JSON with filter** (12-student.py):
    - Python class Student that extends the previous one with an additional method `to_json(attrs=None)` that filters attributes.

13. **Student to disk and reload** (13-student.py):
    - Python class Student that extends the previous one with a method `reload_from_json(json)` to replace all attributes of the instance with those from a JSON dictionary.

14. **Pascal's Triangle** (14-pascal_triangle.py):
    - Python function that returns a list of lists of integers representing Pascal's triangle of size n.

15. **Search and update** (100-append_after.py):
    - Python function that inserts a line of text into a file after each line containing a specified string.

16. **Log parsing** (101-stats.py):
    - Python script that reads lines from standard input and computes metrics after every 10 lines or upon keyboard interruption.

17. **Hack the VM** (read_write_heap.py):
    - Python script that finds and replaces a string in the heap of a running process.

