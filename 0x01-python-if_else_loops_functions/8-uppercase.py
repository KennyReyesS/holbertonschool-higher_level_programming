#!/usr/bin/python3
def uppercase(str):
    for c in str: 
        if ord(c) >= 97:
            c = chr(ord(c) - 32)
        print("{:s}".format(c), end="")
    print("")
