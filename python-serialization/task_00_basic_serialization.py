#!/usr/bin/python3
    """ 
    basic serialization module
    """
import json

def serialize_and_save_to_file(data, filename):
    """
    serialize a dictionary and save it to a JSON file
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

