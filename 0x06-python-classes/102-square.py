#!/usr/bin/python3
"""
This module contain a Square with size privite instance attribute
"""


class Square:
    """
    A class with privte instance attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initalization function
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not all(isinstance(num, int) and num >= 0 for num in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        function that calculate the square area
        """
        return self.__size**2

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

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, position):
        """position setter"""
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not all(isinstance(num, int) and num >= 0 for num in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """function that print the square by # chars"""
        size = self.__size
        position = self.__position
        if not size:
            print()
            return
        print("{:s}".format("\n" * position[1]), end="")
        for x in range(size):
            print(f'{" " * position[0]}{"#" * size}')

    def __str__(self):
        """print class as a square by #"""
        string = ""
        size = self.__size
        position = self.__position
        if not size:
            string += "\n"
            return ""
        string += "\n" * position[1]
        for x in range(size):
            string += f'{" " * position[0]}{"#" * size}\n'
        print(string[:-1], end="")
        return ""

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
