#!/usr/bin/python3
"""
base.py module
"""


import json

"""
class Base.

This class will be the “base” of all other classes in this project.
"""


class Base:
    """private class attribute"""
    __nb_objects = 0

    """Initializes the Base data"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        new = []
        if list_objs is None:
            list_objs = new
        else:
            for i in list_objs:
                new.append(i.to_dictionary())
            json_str = cls.to_json_string(new)
            my_file = cls.__name__ + ".json"
            with open(my_file, 'w', encoding='utf-8') as f:
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
