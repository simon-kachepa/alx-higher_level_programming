#!/usr/bin/python3
"""Defining Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a new Rectangle

            Args:
                width (int): The width of the new Rectangle
                height (int): The height of the new Rectangle
                x (int): x value of the new Rectangle
                y (int):y value for the new Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the current Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """Set the width of the current Rectangle
            Args:
                width(int): The width of the current Rectangle

            Return: Nothing
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Get the height of the current Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height of the current Rectangle

            Args:
                value (int): The height of the current Rectangle

            Return: Nothing
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Get the x value of the current Rectangle"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """Setting the x value of the current Rectangle

            Args:
                x (int): The x value
            Return:
                :Nothing
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Get the y value of the current Rectangle"""
        return (self.__x)

    @y.setter
    def y(self, y):
        """Setting the value of y

            Args:
                y(int): The value of y

            Return:
                :Nothing
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
