#!/usr/bin/python3
"""
makin a func that creates an obj from a JSON
"""

import json


def load_from_json_file(filename):
    """
    func creates an obj from a json file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
