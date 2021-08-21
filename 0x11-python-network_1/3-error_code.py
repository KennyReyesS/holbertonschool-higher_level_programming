#!/usr/bin/python3
"""
3-error_code.py module
"""


from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)

    try:
        request.urlopen(req)
    except error.HTTPError as e:
        print(e.code)
