#!/usr/bin/python3
# 10-student.py
# Nwafor Chukwuebuka
"""Defines a class Student Class."""


class Student:
    """Represent a student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object

        Args:
            first_name (str): Student’s first name
            last_name (str): student’s last name
            age (int): Student’s Age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional Args) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
