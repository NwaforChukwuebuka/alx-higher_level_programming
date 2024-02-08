#!/usr/bin/python3
# 0-lookup.py
# Nwafor Chukwuebuka
"""Defines an object attribute & methods lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes and methods."""
    return (dir(obj))
