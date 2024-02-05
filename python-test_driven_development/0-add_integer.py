#!/usr/bin/python3
"""integer addition function"""


def add_integer(a, b=98):
    """adds two integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("b must be an integer")
    return ((int(a)) + (int(b)))