#!/usr/bin/python3#!/usr/bin/python3
# 6-max_integer_test.py
# Nwafor Chukwuebuka
""" max_integer([..]) unittest"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [11, 12, 13, 14]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [11, 21, 41, 31]
        self.assertEqual(max_integer(unordered), 41)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [64, 23, 22, 21]
        self.assertEqual(max_integer(max_at_beginning), 64)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

    def test_floats(self):
        """Test a list of floats."""
        floats = [11.53, 3.33, -10.123, 16.8, 7.0]
        self.assertEqual(max_integer(floats), 16.8)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [11.53, 45.5, -6, 12, 4]
        self.assertEqual(max_integer(ints_and_floats), 45.5)

    def test_string(self):
        """Test a string."""
        string = "Chukwuebuka"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Chukwuebuka", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
