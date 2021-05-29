#!/usr/bin/python3
"""
Prints a square with the character #.
"""


def text_indentation(text):
    """
    Args:
    text(str): Size of the square
    Returns:
    a text with 2 new lines after of: '.', '?' and ':'.
    """
    flag = 0
    char = [".", "?", ":"]
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if flag == 1:
            flag = 0
            continue
        if i in char:
            print(i, end="")
            print()
            print()
            flag = 1
        else:
            print(i, end="")
