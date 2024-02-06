#!/usr/bin/python3
"""Define function that returns JSON representation of an object"""
import json


def to_json_string(my_obj):
    """function that returns JSON representation of an object (string):

        Args:
            my_obj: object to be returned its JSON representation

            Return: JSON representation of an object (string)
    """
    return (json.dumps(my_obj))
