#!/usr/bin/python3
"""
6-post_email.py module
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    emailaddrs = argv[2]
    values = {'email': emailaddrs}
    response = requests.post(url, data=values)
    print(response.text)
