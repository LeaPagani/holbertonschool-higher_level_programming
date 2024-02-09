#!/usr/bin/python3
"""Rectangle module.
This module contains a class that defines a rectangle.
"""


class Rectangle __init__(self, width=0, heigth=0):
    """Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle."""
    self.width = width
    self.heigth = heigth

@property
def width(self):
    """Docstring for Rectangle width"""
    return self._width

@width.setter
def width (self, value):
    if type(value) is int:
        if value > 0:
            self._width = value
        else:
            raise ValueError (width must be >= 0)
    else:
        raise TypeError (width must be an integer)

@property 
def heigth(self):
    """Docstring for Rectangle heigth"""
    return self._heigth

@heigth.setter
def heigth (self, value):
    if type(value) is int:
        if value > 0:
            self._heigth = value
        else:
            raise ValueError (heigth must be >= 0)
    else:
        raise TypeError (heigth must be an integer)
