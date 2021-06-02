#!/usr/bin/python3
"""
module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initializes the Square data"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns [Square] <width>/<height>"""
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Returns the Square area"""
        return (self.__size * self.__size)
