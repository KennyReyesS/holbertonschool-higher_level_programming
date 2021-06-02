#!/usr/bin/python3
"""
Importing json.
"""
import json

"""
4-from_json_string.py module.
"""


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    return json.loads(my_str)
