#!/usr/bin/python3
"""Add int function"""
def add_integer(a, b=98):
    """Function that returns the sum of two integers"""

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
