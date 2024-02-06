#!/usr/bin/python3
"""
This module contain a function
Insert text after each line containing a given string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file."""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
