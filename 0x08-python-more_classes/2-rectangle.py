#!/usr/bin/python3
"""0-rectangle.py: module containe empty rectangle object"""


class Rectangle:
    """Rectangle object"""

    def __init__(self, width=0, height=0):
        """intialize functon"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)
