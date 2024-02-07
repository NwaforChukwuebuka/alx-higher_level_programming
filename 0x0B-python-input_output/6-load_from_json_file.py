#!/usr/bin/python3
# 6-load_from_json_file.py
# Nwafor Chukwuebuka
"""Defines a Python object loader from a json file  function."""
import json


def load_from_json_file(filename):
    """Loads a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
