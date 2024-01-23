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

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __lt__(self, other):
        """less than"""
        return self.size < other.size

    def __le__(self, other):
        """less than or equal"""
        return self.size <= other.size

    def __eq__(self, other):
        """equal"""
        return self.size == other.size

    def __ne__(self, other):
        """not equal"""
        return self.size != other.size

    def __gt__(self, other):
        """greater than"""
        return self.size >= other.size

    def __ge__(self, other):
        """greater than or equal"""
        return self.size >= other.size
