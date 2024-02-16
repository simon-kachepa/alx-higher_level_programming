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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the current Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width of the current Rectangle
            Args:
                width(int): The width of the current Rectangle

            Return: Nothing
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

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
    def x(self, value):
        """Setting the x value of the current Rectangle

            Args:
                x (int): The x value
            Return:
                :Nothing
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Get the y value of the current Rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Setting the value of y

            Args:
                y(int): The value of y

            Return:
                :Nothing
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area of the current Rectangle"""
        return (self.width * self.height)

    def display(self):
        """Displays the Rectangle with the character #"""
        for a in range(self.y):
            print()
        for i in range(self.height):
            for b in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        """Collecting arguments and assigns to attributes"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
