# Python Object Instantiation and Memory Management

This project explores various concepts related to object instantiation, memory management, variable aliasing, object identifiers, types, and mutability in Python. It consists of a series of quiz-like questions along with their corresponding answers provided in single-line .txt files.

## Tests

The `tests` folder contains test files provided by Holberton School to verify the correctness of the solutions.

## Tasks

### 0. Who am I?

**Question:** What function would you use to print the type of an object?

**Answer:** `type()`

### 1. Where are you?

**Question:** How do you get a variable's identifier (which is the memory address in the CPython implementation)?

**Answer:** You can get a variable's identifier using the `id()` function.

### 2. Right count

**Question:** In the following code, do `a` and `b` point to the same object?
```python
a = 89
b = 100

3. Right count =
Question: In the following code, do a and b point to the same object?

python
Copy code
a = 89
b = 89
Answer: Yes.

...

Pythonic Functions
Additionally, the project includes Python functions to demonstrate certain concepts:

copy_list(l): Returns a copy of a list.
magic_string(): Returns the string "Holberton" n times the number of iteration.
LockedClass: A class with no attributes that prevents dynamically creating new instance attributes not called first_name.
Memory Management
The project also includes questions related to memory management, such as tracking the creation and deletion of objects and understanding object reuse.

Files
The project includes various files named according to the tasks they address, along with corresponding answers in .txt files.
