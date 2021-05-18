#!/usr/bin/python3
""" Square size.

creating square with size and area

"""


class Square:
    """Initializes the Square data"""
    def __init__(self, size=0):
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """Making private instance attribute"""
        self.__size = size

    """Get the area of a square"""
    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)
