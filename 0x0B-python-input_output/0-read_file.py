#!/usr/bin/python3
"""
Module 0-read_file.py.
"""


def read_file(filename=""):
    """"reads a text file (UTF8) and prints it to stdout"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
