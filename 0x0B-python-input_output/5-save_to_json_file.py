#!/usr/bin/python3
# 5-save_to_json_file.py
# Nwafor Chukwuebuka
"""Defines a JSON object dumping into file function"""
import json


def save_to_json_file(my_obj, filename):
    """Duping JSON object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
