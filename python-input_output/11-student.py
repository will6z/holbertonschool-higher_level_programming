#!/usr/bin/python3
"""
makin a student (same as 10)
"""
class Student:
    def __init__(self, first_name, last_name, age):
        """ definin a func """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

