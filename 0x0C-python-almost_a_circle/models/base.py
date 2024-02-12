#!/usr/bin/python3

"""Defining a class Base"""


class Base:
    """Represent the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new base

            Args:
                id (int): the ID of the class
        """
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
