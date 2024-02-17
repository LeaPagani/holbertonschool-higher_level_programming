#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle and defines a Square object."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get and Set the size attribute of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

# Methods
    def update(self, *args, **kwargs):
        """Assigns arguments to attributes."""
        if args:
            attrs = ['id', 'width', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
