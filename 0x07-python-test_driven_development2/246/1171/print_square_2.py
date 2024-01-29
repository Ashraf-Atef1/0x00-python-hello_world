#!/usr/bin/python3
""" Doc """

def print_square(size):
    """ Doc """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    for r in range(0, size):
        for c in range(0, size):
            if c != (size - 1):
                print("#", end="")
            else:
                print("#")
