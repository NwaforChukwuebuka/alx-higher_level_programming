#!/usr/bin/python3
# 10-class_to_json.py
# Nwafor chukwuebuka
"""Defines a Python class-to-JSON converter"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__