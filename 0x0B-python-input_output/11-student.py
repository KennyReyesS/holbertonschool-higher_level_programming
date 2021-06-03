#!/usr/bin/python3
"""
class Student.
"""


class Student:
    """initializes the Student data"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is not list:
            return self.__dict__

        new_dict = {}

        for key, val in self.__dict__.items():
            if key in attrs:
                new_dict[key] = val
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
