#!/usr/bin/python3
""" Defines a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file and prints to std out"""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
