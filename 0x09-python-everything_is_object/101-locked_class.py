#!/usr/bin/python3
"""LockedClass.
prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called
"""


class LockedClass:
    """__slots__ attribute"""
    __slots__ = ["first_name"]
