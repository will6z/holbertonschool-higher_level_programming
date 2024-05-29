#!/usr/bin/python3

"""
makin a func that returns an obj represented by a JSON string
"""

import json

def from_json_string(my_str):
    """
    func returns an obj
    """
    return json.loads(my_str)
