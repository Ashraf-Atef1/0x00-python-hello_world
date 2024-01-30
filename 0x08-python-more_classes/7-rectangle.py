#!/usr/bin/python3
"""0-rectangle.py: module containe empty rectangle object"""


class Rectangle:
    """Rectangle object"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        """get rect_area"""
        return self.__width * self.__height

    def perimeter(self):
        """get rect_perimeter"""
        return (self.__width and self.__height
                and 2 * (self.__width + self.__height))

    def __str__(self):
        """return a represent string"""
        width, height = self.__width, self.__height
        to_be_print = ""
        while height and width:
            height -= 1
            to_be_print += (str(self.print_symbol) * width
                            + ("\n" if height else ""))
        return to_be_print

    def __repr__(self):
        """return a define string"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """return a string when delete an object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
