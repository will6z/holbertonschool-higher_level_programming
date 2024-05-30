#!/usr/bin/python3
"""Serialize and Deserialize using pickle"""
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialize attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize object to a file"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as error:
            print(f"Error serializing object: {error}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from a file"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as error:
            print(f"Error deserializing object: {error}")
            return None

