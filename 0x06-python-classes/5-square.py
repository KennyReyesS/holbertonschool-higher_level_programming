#!/usr/bin/python3
""" Square size.
creating square with size and area.
"""


class Square:
    """Initializes the Square data"""
    def __init__(self, size=0):
        """Making private instance attribute"""
        self.__size = size

    @property
    def size(self):
        """returns square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets conditions for the value of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Get the area of a square"""
    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)

    """Print a square"""
    def my_print(self):
        """set condition if size is equal to 0"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
