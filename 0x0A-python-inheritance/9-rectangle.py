#!/usr/bin/python3
"""
Module for BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """initializes the Rectangle data"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """Returns [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns the Rectangle area"""
        return (self.__width * self.__height)
