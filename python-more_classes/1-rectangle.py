#!/usr/bin/python3
"""Rectangle module.
This module contains a class that defines a rectangle.
"""


class Rectangle ():
    """Defines a rectangle."""

def __init__(self, width=0, heigth=0):
    """Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
    """
    self.width = width
    self.height = height



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
            raise ValueError ("width must be >= 0")
    else:
        raise TypeError ("width must be an integer")

@property 
def height(self):
    """Docstring for Rectangle height"""
    return self._height

@height.setter
def height (self, value):
    if type(value) is int:
        if value > 0:
            self._height = value
        else:
            raise ValueError ("height must be >= 0")
    else:
        raise TypeError ("height must be an integer")
