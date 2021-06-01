#!/usr/bin/python3
"""
Class BaseGeometry.
"""


class BaseGeometry:
    """Method: area of BaseGeometry"""
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    """Method: integer validator"""
    def integer_validator(self, name, value):
        """validates value"""
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
