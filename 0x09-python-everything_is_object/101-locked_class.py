#!/usr/bin/python3
# 101-locked_class.py
# NwaforChukwuebuka
"""Defines a locked class."""


class LockedClass:
    """
    Restricts the user from instantiating new LockedClass attributes
    except the attribute called 'first_name'.
    """

    __slots__ = ["first_name"]
