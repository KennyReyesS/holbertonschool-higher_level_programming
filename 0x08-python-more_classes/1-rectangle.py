#!/usr/bin/python3
"""Rectangle class.
That creates rectangle class with height and width.
"""


class Rectangle:
    """Initializes the Rectangle data"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets conditions for the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Returns width in private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets conditions for the width of the Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        else:
            self.__width = value
