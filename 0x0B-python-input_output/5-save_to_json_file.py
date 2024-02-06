#!/usr/bin/python3
"""Define function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation:

        Args:
            my_obj: JSON object
            filename: The name of the function to write the my_obj

            Return: Nothing
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
