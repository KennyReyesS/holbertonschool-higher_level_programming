#!/usr/bin/python3
"""Square class.

Prints squares in stdout.

"""


class Square:
    """Initializes the Square data"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets conditions for the value of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets conditions for the value of the square position"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Get the area of a square"""
    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)

    """Prints squares"""
    def my_print(self):
        """set condition if size is equal to 0"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for l in range(self.__size):
                print("#", end="")
            print("")
