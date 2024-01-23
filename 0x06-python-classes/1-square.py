#!/usr/bin/python3
"""
This module contain a Square with size privite instance attribute
"""


class Square:
    """
    A class with privte instance attribute
    """
    def __init__(self, size):
        """
            initalization function
        """
        self.__size = size
