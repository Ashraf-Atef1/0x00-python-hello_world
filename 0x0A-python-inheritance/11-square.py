#!/usr/bin/python3
"""
This module contain Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """initialization"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the rectangle area"""
        return self.__width*self.__height

    def __str__(self):
        """object string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
