#!/usr/bin/python3
""" Class Base """


class Base():
    """ This class will be the “base” of all other classes in this project. 
    The goal of it is to manage id attribute in all your future classes and 
    to avoid duplicating the same code (by extension, same bugs) """

    __nb_objects = 0
    """ Private class Atribute """

    def __init__(self, id=None):
        """ Class constructor
        Args: 
        id(int) 
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
