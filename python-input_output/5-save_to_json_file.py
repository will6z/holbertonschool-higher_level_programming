#!/usr/bin/python3
"""
makin a func that writes an obj to a txt file using JSON
"""

import json


def save_to_json_file(my_obj, filename):
    """
    func writes an obj to a text
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
