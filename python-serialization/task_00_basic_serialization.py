#!/usr/bin/python3
    """ 
    basic serialization module that adds the functionality to serialize a 
    Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary. 
    """

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file
    """

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Load data from a JSON file and deserialize it to a Python dict 
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

