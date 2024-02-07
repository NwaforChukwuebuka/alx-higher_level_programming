#!/usr/bin/python3
# 13-student.py
# Nwafor Chukwuebuka
"""Defines a class Student."""


class Student:
    """Represent a student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object.

        Args:
            first_name (str): Sudent’s first name
            last_name (str): Student’s last name
            age (int): Student’s Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, retrieves only those attributes
        included in the list.

        Args:
            attrs (list): (Optional Args) The attrs to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {ky: getattr(self, ky) for ky in attrs if hasattr(self, ky)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
