#!/usr/bin/python3
"""
5-hbtn_header.py module
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
