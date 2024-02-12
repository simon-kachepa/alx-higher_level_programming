#!/usr/bin/python3
from models.base import Base
"""Defining Rectangle class"""


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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width of the current Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """Get the height of the current Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """Get the x value of the current Rectangle"""
        return (self.__x)

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """Get the y value of the current Rectangle"""
        return (self.__x)

    @y.setter
    def y(self, y):
        self.__y = y
