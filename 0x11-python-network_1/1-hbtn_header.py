#!/usr/bin/python3
"""
1-hbtn_header.py module
"""

from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        html = response.info()
    print(html.get('X-Request-Id'))
