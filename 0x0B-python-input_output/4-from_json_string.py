#!/usr/bin/python3
# 6-from_json_string.py
# Nwafor Chukwuebuka
"""Defines a JSON-to-python string object function."""
import json


def from_json_string(my_str):
    """Return the string object representation of a JSON object"""
    return json.loads(my_str)
