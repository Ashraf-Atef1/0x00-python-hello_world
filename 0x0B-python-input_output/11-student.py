#!/usr/bin/python3
"""
This module contain a class Student that defines a student
"""


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """initalization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """convert instance into a json object"""
        my_dict = {}
        for key, value in self.__dict__.items():
            if not isinstance(attrs, list) or key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """update instance attrbutes from a json file"""
        for key, value in json.items():
            setattr(self, key, value)
