#!/usr/bin/python3
"""
This module has a function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "rt") as f:
        print(f.read())
