#!/usr/bin/python3
"""makin a func that returns a dictionary desc"""


def class_to_json(obj):
    """returns a dictionary descritpion with a simple date structure"""
    att = obj.__dict__
    json_dict = {}

    for key, value in att.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
