#!/usr/bin/python3
"""
This module has a function that append a string to a text file (UTF8)
and returns the number of characters appended
"""


def append_write(filename="", text=""):
    """
    A function that append a string to a text file (UTF8)
    and returns the number of characters appended
    """
    with open(filename, "at") as f:
        return f.write(text)
