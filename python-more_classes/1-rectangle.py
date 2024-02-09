#!/usr/bin/python3
"""Rectangle class"""

class Reactangle __init__(self, width=0, heigth=0):
    self._width = width
    self._heigth = heigth

@property 
def width(self):
    if type(width) isinstance(int):
        if width > 0:
            self._width = width
        else:
            raise ValueError (width must be >= 0)
    else:
        raise TypeError (width must be an integer)

@property 
def heigth(self):
    if type(heigth) isinstance(int):
        if heigth > 0:
            self._width = heigth
        else:
            raise ValueError (heigth must be >= 0)
    else:
        raise TypeError (heigth must be an integer)




