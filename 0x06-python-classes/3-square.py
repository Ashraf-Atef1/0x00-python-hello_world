#!/usr/bin/python3
"""
This module contain a Square with size privite instance attribute
"""


class Square:
    """
    A class with privte instance attribute
    """
    def __init__(self, size=0):
        """
            initalization function
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        function that calculate the square area
        """
        return self.__size ** 2
