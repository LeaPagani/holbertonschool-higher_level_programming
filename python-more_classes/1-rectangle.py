#!/usr/bin/python3
"""Docstring for file"""


class Rectangle __init__(self, width=0, heigth=0):
    """Docstring for rectangle class"""
    self.width = width
    self.heigth = heigth

@property
def width(self):
    """Docstring for Rectangle width"""
    return self._width

@width.setter
def width (self, value):
    """Docstring for Rectangle width setter"""
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
    """Docstring for Rectangle heigth setter"""
    if type(value) is int:
        if value > 0:
            self._heigth = value
        else:
            raise ValueError (heigth must be >= 0)
    else:
        raise TypeError (heigth must be an integer)
