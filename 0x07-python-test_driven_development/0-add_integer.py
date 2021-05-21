#!/usr/bin/python3
"""
Adds 2 integers and cast to int if they are float.
"""


def add_integer(a, b=98):
    """
    Args:
    a(int): The first parameter to add.
    b(int): The second parameter to add.

    Returns:
    The result of: a + b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")

    res = a + b
    return (res)
