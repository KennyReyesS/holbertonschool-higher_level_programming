#!/usr/bin/python3
"""
8-class_to_json.py module
"""


def class_to_json(obj):
    """"returns the dict description with simple data structure"""
    return obj.__dict__
