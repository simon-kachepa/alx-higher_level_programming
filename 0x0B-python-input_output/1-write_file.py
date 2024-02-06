#!/usr/bin/python3
"""Defines a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Returns the number of characters written:

        Args:
            filename (str): The name of the file to write to
            text (str): The content to be written to the file

        Return: The number of characters written to filename
    """
    with open(filename, "w", encoding="UTF8") as f:
        return (f.write(text))
