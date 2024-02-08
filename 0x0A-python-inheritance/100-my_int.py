#!/usr/bin/python3
# 100-my_int.py
# Nwafor Chukwuebuka
"""Defines a subclass class MyInt that inherits from Int parent class"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, value):
        """Overriding == operator with != behaviour."""
        return self.real != value

    def __ne__(self, value):
        """Overriding != operator with == behaviour."""
        return self.real == value
