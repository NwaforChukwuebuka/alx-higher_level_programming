#!/usr/bin/python3
# 5-to_json_string.py
# Nwafor Chukwuebuka
"""Defines a string-to-JSON dumper function"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
