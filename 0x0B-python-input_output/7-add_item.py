#!/usr/bin/python3
# 9-add_item.py
# Nwafor Chukwuebuka
"""Add all args to a Python list and save them to a json file."""
import sys

if __name__ == "__main__":
    json_dumper = __import__('5-save_to_json_file').save_to_json_file
    json_loader = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        argz = json_loader("add_item.json")
    except FileNotFoundError:
        argz = []
    argz.extend(sys.argv[1:])
    json_dumper(argz, "add_item.json")
