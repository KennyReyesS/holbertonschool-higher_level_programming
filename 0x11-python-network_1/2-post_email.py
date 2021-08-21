#!/usr/bin/python3
"""
2-post_email.py module
"""


from urllib import parse, request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    values = '{email: argv[1]}'

    data = parse.urlencode(values)

    data = data.encode('ascii')

    req = request.Request(url, data)

    with request.urlopen(req) as response:
        html = response.read()
    print(html)
