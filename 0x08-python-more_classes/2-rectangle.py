#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle.
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle data"""
        self.height = height
        self.width = width

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
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """Get the area of a Rectangle"""
    def area(self):
        """Return the rectangle area"""
        return (self.__height * self.__width)

    """Get the perimeter of a Rectangle"""
    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)
