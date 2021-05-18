#!/usr/bin/python3
""" Square size.

Attribute:
size (int):
"""


class Square:
    """initializes the Square data"""
    def __init__(self, size=0):
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """making private instance attribute"""
        self.__size = size
