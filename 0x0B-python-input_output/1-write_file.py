#!/usr/bin/python3
"""
Module 0-read_file.py.
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
