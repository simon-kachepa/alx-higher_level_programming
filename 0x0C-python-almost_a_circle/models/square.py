#!/usr/bin/python3
"""Defining the square module (modules.square)"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing a new Square

            Args:
                size: size of the square
                x (int): x value of the square
                y (int): y value of the square
                id(int): id of the square
        """
        super().__init__(size, size, x=0, y=0, id=None)

    def __str__(self):
        """Method that returns a string"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getting the size of the current square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting the size of the current square
            Args:
                size(int): The size of each side off the square

        """
        self.width = value
        self.height = value
