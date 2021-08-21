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
        with request.urlopen(url) as response:
            html = response.read()
        print(html.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
