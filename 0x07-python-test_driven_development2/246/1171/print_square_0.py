#!/usr/bin/python3
""" Doc """

def print_square(size):
    """ Doc """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("Fail")
