#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)

        Args:
            filename (str): The name of the file
            text (str): The text to append to filename

        Return:
            the number of characters added:
    """
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
